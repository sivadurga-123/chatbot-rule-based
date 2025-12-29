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

## Installation & Setup Guide

### ⚙️ Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Git (optional, for cloning the repository)

### 🚀 Quick Start

#### 1. Clone the Repository
```bash
git clone https://github.com/sivadurga-123/chatbot-rule-based.git
cd chatbot-rule-based
```

#### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```

The backend will start on `http://localhost:5000`

#### 3. Frontend Setup

**Option A: Open HTML file directly**
```bash
# Navigate to frontend directory
cd ../frontend

# Open in your default browser
# On Windows:
start index.html

# On macOS:
open index.html

# On Linux:
xdg-open index.html
```

**Option B: Use a local web server (Recommended)**
```bash
# From frontend directory
python -m http.server 8000

# Open browser and go to: http://localhost:8000
```

### 📝 Environment Variables

The API base URL is set to `http://localhost:5000` by default in `script.js`.
If you want to change it:

1. Edit `frontend/script.js`
2. Find: `const API_BASE_URL = 'http://localhost:5000';`
3. Change to your server URL

### 🧪 Testing the Chatbot

1. Ensure both backend (Flask) and frontend servers are running
2. Open the chatbot interface in your browser
3. Try typing messages like:
   - "Hello"
   - "What is AI?"
   - "Tell me a joke"
   - "Who are you?"

### 🐛 Troubleshooting

**CSS/JS not loading?**
- Make sure you're accessing the HTML file through a web server, not just opening it directly
- Clear your browser cache (Ctrl+Shift+Delete)

**Backend connection error?**
- Verify Flask server is running: `python app.py` in the backend directory
- Check that the API URL in `script.js` matches your backend URL
- Ensure port 5000 is not in use: `lsof -i :5000` (macOS/Linux) or `netstat -ano | findstr :5000` (Windows)

**Dependencies installation failed?**
- Upgrade pip: `pip install --upgrade pip`
- Use a virtual environment: `python -m venv venv` then activate it
- Try installing with: `pip install -r requirements.txt --no-cache-dir`

### 📦 Requirements

The project requires the following Python packages (see `backend/requirements.txt`):
- Flask: Web framework
- Flask-CORS: Handle cross-origin requests
- Werkzeug: WSGI utility library

### 📱 Mobile Responsive

The chatbot is fully responsive and works on:
- Desktop browsers
- Tablets
- Mobile phones (iOS Safari, Chrome Mobile)

### 🎨 Customization

**Change the color scheme:**
Edit the CSS variables in `frontend/style.css`:
```css
:root {
  --primary-color: #667eea;      /* Change this */
  --secondary-color: #764ba2;    /* And this */
  --accent-color: #f093fb;       /* And this */
}
```

**Add more chatbot responses:**
Edit `backend/app.py` and add patterns to the rules dictionary:
```python
self.rules = {
    r'your pattern here': 'Your response here',
    # Add more...
}
```

### 📚 Project Files

- `backend/app.py` - Flask server with chatbot logic
- `backend/requirements.txt` - Python dependencies
- `frontend/index.html` - Chat interface structure
- `frontend/style.css` - Chat interface styling
- `frontend/script.js` - Frontend interactivity and API calls
- `README.md` - Project documentation

### ✨ Features

✅ Rule-based pattern matching
✅ Real-time message display
✅ Loading indicator while bot responds
✅ Auto-scroll to latest messages
✅ Quick suggestion buttons
✅ Responsive design
✅ Beautiful gradient UI
✅ Message timestamps
✅ Error handling with user feedback
✅ RESTful API backend

### 📄 License

MIT License - Created as part of CODSOFT AI Internship

### 👥 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Made with ❤️ by CODSOFT AI Internship**

For more information, visit: [CODSOFT](https://codsoft.in)

## License
MIT License
