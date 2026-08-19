AI Agent

A lightweight AI agent built with FastAPI and the Gemini API. It can understand a user's request, decide which tool is required, execute that tool, and return the result through a simple web-based chat interface.

Features

The agent currently supports 5 tools:

🧮 Calculator — Performs mathematical calculations.
🌤️ Weather — Gets current weather information for a city.
💱 Currency Converter — Converts amounts between currencies.
📏 Measurement Converter — Converts units such as feet, meters, miles, kilograms, pounds, Celsius, and Fahrenheit.
📝 Text Utility — Performs operations such as word counting, character counting, uppercase/lowercase conversion, reversing text, removing extra spaces, word occurrence counting, and palindrome checking.
How It Works
User Request
     ↓
   Gemini
     ↓
Chooses appropriate tool
     ↓
Python Tool Execution
     ↓
Result sent back to Gemini
     ↓
Final Response

Gemini acts as the decision-maker, so the backend does not manually determine which tool should be used.

Tech Stack
Python
FastAPI
Google Gemini API
HTML / CSS / JavaScript
Python Requests
Project Structure
PLEXIMUS/
├── backend/
│   ├── main.py
│   ├── agent.py
│   └── tools/
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
└── .gitignore
Running Locally

Create a .env file:

GEMINI_API_KEY=your_api_key_here

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn backend.main:app --reload

Open:

http://127.0.0.1:8000

The .env file should not be committed to GitHub because it contains the Gemini API key.
