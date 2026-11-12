# Basic LangChain Chatbot 🤖

A simple AI chatbot built using LangChain, Groq and Streamlit.

## Features

- LLM integration using Groq
- Prompt templates using LangChain
- LCEL chain implementation
- Conversation history
- Streaming AI responses
- Interactive Streamlit interface

## Tech Stack

- Python
- LangChain
- Groq API
- Streamlit
- Python-dotenv

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd basic_langchain_chatbot
```

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
uv run streamlit run app.py
```

## Project Structure

```text
basic_langchain_chatbot/
├── .env
├── .gitignore
├── app.py
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```
