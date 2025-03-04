# 📚 API Documentation Scraper for LLMs

A powerful tool for scraping and collecting API documentation to use with Large Language Models (LLMs). This project helps you gather comprehensive documentation from various sources to improve your LLM's knowledge about specific APIs and frameworks.

## ✨ Features

- 🔍 Scrapes documentation from any API or framework website
- 🔄 Recursively follows links to gather comprehensive documentation
- 🤖 Uses OpenAI's GPT models to filter and process relevant content
- 🌐 Supports both command-line interface and web application
- 📁 Saves documentation in easily accessible text files
- 🚀 Concurrent scraping for faster performance

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Jina AI API key

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/AshleyDelph84/LLM-Scraper.git
   cd LLM-Scraper
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   JINA_API_KEY=your_jina_api_key_here
   ```

## 🚀 Usage

### Command Line Interface

Run the script with Python:

```
python API-Doc-Scraper.py
```

Follow the prompts to enter the URL of the documentation you want to scrape. The script will:
1. Scrape the initial URL
2. Extract additional URLs from the content
3. Filter relevant documentation URLs using OpenAI
4. Scrape all relevant URLs concurrently
5. Save the documentation to a text file named after the domain

### Web Application

Start the Flask web server:

```
python app.py
```

Open your browser and navigate to `http://localhost:5000`. The web interface allows you to:
1. Enter a documentation URL
2. View scraping progress in real-time
3. Download the scraped documentation
4. View the documentation directly in the browser

## 📂 Project Structure

- `API-Doc-Scraper.py`: Command-line version of the scraper
- `app.py`: Flask web application
- `requirements.txt`: Required Python packages
- `templates/`: HTML templates for the web interface
- `Agno-Framework-Documentation/`, `OpenAi-Swarm/`: Example scraped documentation

## 🔧 Configuration

You can adjust the scraping behavior by modifying the following parameters in the scripts:

- `max_retries`: Number of retry attempts for failed requests
- `X-Timeout`: Timeout value for Jina AI requests
- OpenAI model: Currently using "gpt-4o-mini" for URL filtering

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.