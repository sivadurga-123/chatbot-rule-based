# Task 1: Chatbot with Rule-Based Responses

A simple rule-based chatbot that responds to user inputs based on predefined rules using pattern matching and if-else statements.

## Project Overview
This project implements a conversational AI system that uses rule-based pattern matching to identify user queries and provide appropriate responses. It's designed to understand basic natural language processing concepts and conversation flow.

## Tech Stack
- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML, CSS, JavaScript
- **Architecture**: REST API

## Project Structure
```
.
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt     # Python dependencies
│   └── chatbot.py          # Chatbot logic
├── frontend/
│   ├── index.html          # Main UI
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── README.md
└── .gitignore
```

## Installation & Setup

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup
1. Open `frontend/index.html` in a web browser
2. Ensure backend server is running on http://localhost:5000

## Features
- Pattern-based rule matching
- Multiple predefined conversation patterns
- Easy to extend with new rules
- Clean web interface
- RESTful API

## API Endpoints
- **POST /chat** - Send message to chatbot
  - Request: `{"message": "user message"}`
  - Response: `{"response": "bot response"}`

## How to Use
1. Start the Flask backend server
2. Open the HTML frontend
3. Type your message and press Enter or click Send
4. Chatbot responds based on pattern matching rules

## Sample Conversations
- "Hello" → "Hello! How can I help you today?"
- "What is your name?" → "I'm a rule-based chatbot created for CODSOFT internship."
- "Bye" → "Goodbye! Have a great day!"

## Future Enhancements
- NLP integration with NLTK or spaCy
- Machine learning-based intent classification
- Database for storing conversation history
- Multi-language support

## Author
Created as part of CODSOFT AI Internship

## License
MIT License
