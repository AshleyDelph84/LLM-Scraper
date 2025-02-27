import os
import asyncio
import aiohttp
import re
from urllib.parse import urlparse
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
from threading import Thread

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Import scraper functions from the original script
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

async def scrape_url_async(session, url, max_retries=3):
    jina_api_url = f"https://r.jina.ai/{url}"
    headers = {
        "Authorization": f"Bearer {os.getenv('JINA_API_KEY')}",
        "X-Timeout": "10"
    }
    
    for attempt in range(max_retries):
        try:
            async with session.get(jina_api_url, headers=headers) as response:
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            if attempt == max_retries - 1:
                return None
            await asyncio.sleep(2 ** attempt)  # Exponential backoff

async def scrape_urls_concurrently(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_url_async(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def extract_urls(content):
    url_pattern = r'https?://[^\s)\]"]+'  # Regex pattern to find URLs
    urls = re.findall(url_pattern, content)
    unique_urls = []
    seen = set()
    for url in urls:
        if url not in seen and is_valid_url(url):
            seen.add(url)
            unique_urls.append(url)
    return unique_urls

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split('.')
    if len(domain_parts) > 2 and domain_parts[0] != 'www':
        domain = f"{domain_parts[0]}_{domain_parts[1]}"
    elif domain_parts[0] == 'www':
        domain = domain_parts[1]
    else:
        domain = domain_parts[0]
    return f"{domain}_docs.txt"

def create_content_section(content, url, index):
    separator = "=" * 80
    return f"\n{separator}\nSection {index}: Content from {url}\n{separator}\n\n{content}\n\n"

def write_content_to_file(filename, sections):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("".join(sections))
    return filename

def filter_urls(urls, base_url):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    urls_text = "\n".join(urls)
    base_domain = urlparse(base_url).netloc
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a URL curator tasked with filtering out obviously unrelated content from a list of URLs for a software tool or API."},
            {"role": "user", "content": f"""We need to extract documentation for a tool with the base domain {base_domain}. Here's a list of URLs we've found:

{urls_text}

Please filter this list based on the following criteria:
1. Keep URLs that appear to be related to documentation, guides, tutorials, or API references.
2. Include relevant subdomains like 'docs.{base_domain}', 'api.{base_domain}', or 'developer.{base_domain}'.
3. Remove URLs for obviously unrelated content such as community forums, status pages, blog posts, or contact pages.

Respond with a list of filtered URLs, one per line, without any additional text or formatting. Ensure all URLs are valid."""}
        ]
    )
    filtered_urls = [url.strip() for url in response.choices[0].message.content.strip().split('\n') if is_valid_url(url.strip())]
    return filtered_urls

# Global variable to store scraping progress
scraping_progress = {}

async def scrape_documentation(url):
    global scraping_progress
    session_id = scraping_progress['session_id']
    
    scraping_progress[session_id] = {
        'status': 'starting',
        'message': 'Starting scraping process...',
        'progress': 0,
        'total_urls': 0,
        'scraped_urls': 0,
        'filename': None
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            # Step 1: Scrape initial URL
            scraping_progress[session_id]['status'] = 'scraping_initial'
            scraping_progress[session_id]['message'] = f'Scraping initial URL: {url}'
            
            initial_content = await scrape_url_async(session, url)
            if not initial_content:
                scraping_progress[session_id]['status'] = 'error'
                scraping_progress[session_id]['message'] = 'Failed to scrape the initial URL.'
                return
            
            # Step 2: Extract URLs
            urls = extract_urls(initial_content)
            scraping_progress[session_id]['status'] = 'extracting_urls'
            scraping_progress[session_id]['message'] = f'Found {len(urls)} unique URLs.'
            
            # Step 3: Filter URLs
            filtered_urls = filter_urls(urls, url)
            scraping_progress[session_id]['total_urls'] = len(filtered_urls)
            scraping_progress[session_id]['status'] = 'filtering_urls'
            scraping_progress[session_id]['message'] = f'Filtered down to {len(filtered_urls)} relevant URLs.'
            
            # Step 4: Scrape all filtered URLs
            scraping_progress[session_id]['status'] = 'scraping_urls'
            contents = await scrape_urls_concurrently(filtered_urls)
            
            # Step 5: Process and save content
            sections = []
            for i, (url, content) in enumerate(zip(filtered_urls, contents), 1):
                if content:
                    sections.append(create_content_section(content, url, i))
                    scraping_progress[session_id]['scraped_urls'] += 1
                    scraping_progress[session_id]['progress'] = int((scraping_progress[session_id]['scraped_urls'] / scraping_progress[session_id]['total_urls']) * 100)
                    scraping_progress[session_id]['message'] = f'Scraped {scraping_progress[session_id]["scraped_urls"]} of {scraping_progress[session_id]["total_urls"]} URLs.'
            
            # Step 6: Write to file
            filename = get_filename_from_url(url)
            write_content_to_file(filename, sections)
            
            scraping_progress[session_id]['status'] = 'completed'
            scraping_progress[session_id]['message'] = f'Scraping completed! Content saved to {filename}.'
            scraping_progress[session_id]['filename'] = filename
            
    except Exception as e:
        scraping_progress[session_id]['status'] = 'error'
        scraping_progress[session_id]['message'] = f'An error occurred: {str(e)}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url', '')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    if not is_valid_url(url):
        return jsonify({'error': 'Invalid URL format'}), 400
    
    # Generate a unique session ID
    session_id = os.urandom(16).hex()
    session['scrape_session_id'] = session_id
    
    # Initialize progress tracking
    global scraping_progress
    scraping_progress['session_id'] = session_id
    scraping_progress[session_id] = {
        'status': 'initializing',
        'message': 'Initializing scraper...',
        'progress': 0,
        'total_urls': 0,
        'scraped_urls': 0,
        'filename': None
    }
    
    # Start scraping in a background thread
    def run_async_scrape():
        asyncio.run(scrape_documentation(url))
    
    thread = Thread(target=run_async_scrape)
    thread.daemon = True
    thread.start()
    
    return jsonify({
        'message': 'Scraping started',
        'session_id': session_id
    })

@app.route('/progress')
def progress():
    session_id = session.get('scrape_session_id')
    if not session_id or session_id not in scraping_progress:
        return jsonify({'error': 'No active scraping session'}), 404
    
    return jsonify(scraping_progress[session_id])

@app.route('/download/<filename>')
def download_file(filename):
    from flask import send_from_directory
    return send_from_directory(os.getcwd(), filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)