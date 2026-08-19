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
