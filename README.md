# AI Agent

A lightweight AI agent built with **FastAPI** and the **Google Gemini API**. It can understand a user's request, decide which tool is required, execute that tool, and return the result through a simple web-based chat interface.

## Features

The agent currently supports 5 tools:

- 🧮 **Calculator** — Performs mathematical calculations.
- 🌤️ **Weather** — Gets current weather information for a city.
- 💱 **Currency Converter** — Converts amounts between currencies.
- 📏 **Measurement Converter** — Converts units such as feet, meters, miles, kilograms, pounds, Celsius, and Fahrenheit.
- 📝 **Text Utility** — Performs operations such as word counting, character counting, uppercase/lowercase conversion, reversing text, removing extra spaces, word occurrence counting, and palindrome checking.

## How It Works

The user sends a request to the AI agent. Gemini analyzes the request and decides which tool should be used.

```text
User Request
     ↓
   Gemini
     ↓
Select Appropriate Tool
     ↓
Python Tool Execution
     ↓
Tool Result
     ↓
   Gemini
     ↓
Final Response
```

Gemini acts as the **decision-maker**, while the Python backend handles the actual tool execution.

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript

## Project Structure

```text
AI-Agent/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   │
│   └── tools/
│       ├── __init__.py
│       ├── calculator.py
│       ├── weather.py
│       ├── currency.py
│       ├── measurement.py
│       └── text_utility.py
│
├── frontend/
│   └── index.html
│
├── .env
├── .gitignore
└── README.md
```

## Running Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI-Agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Start the application

```bash
uvicorn backend.main:app --reload
```

### 6. Open the application

Visit:

```text
http://127.0.0.1:8000
```

## API

The main API endpoint is:

```text
POST /chat
```

Example request:

```json
{
    "message": "Convert 10 feet to meters"
}
```

Example response:

```json
{
    "response": "10 feet is equal to 3.048 meters."
}
```

## Tool Examples

### Calculator

```text
What is 15% of 1535?
```

### Weather

```text
What's the weather in Mumbai?
```

### Currency Converter

```text
Convert 100 USD to INR.
```

### Measurement Converter

```text
Convert 10 feet to meters.
```

### Text Utility

```text
How many words are in "The quick brown fox jumps over the lazy dog"?
```

## Security

The Gemini API key is stored in `.env` and excluded from Git using `.gitignore`.

**Never commit your API key to the repository.**
