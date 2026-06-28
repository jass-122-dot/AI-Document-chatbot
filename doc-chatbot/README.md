# AI Document Chatbot

Upload PDF documents and chat with them using Google Gemini AI.

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Database: SQLite (built-in, no installation needed)
- AI: Google Gemini API
- Vector Search: ChromaDB

## Setup Instructions

### 1. Install Python packages
```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set your Gemini API key
Open `backend/.env` and replace:
```
GEMINI_API_KEY=your_gemini_api_key_here
```
with your actual key.

### 3. Run the backend
```
python app.py
```
SQLite database (chatbot.db) is created automatically. No MySQL needed.

### 4. Open frontend
Open `frontend/pages/login.html` with Live Server in VS Code.

## Features
- Register / Login with JWT auth
- Upload PDF documents
- AI chat with your documents using Gemini
- Chat history saved per document
- Delete documents
