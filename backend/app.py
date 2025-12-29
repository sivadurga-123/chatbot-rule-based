"""Rule-Based Chatbot Backend

A Flask-based REST API for a rule-based chatbot that responds to user queries
using pattern matching and predefined response rules.

Author: CODSOFT AI Internship
Date: December 2025
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import json
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend

class RuleBasedChatbot:
    """A rule-based chatbot that responds to user inputs based on pattern matching."""
    
    def __init__(self):
        """Initialize the chatbot with predefined rules and responses."""
        # Define conversation rules as regex patterns mapped to responses
        self.rules = {
            r'hello|hi|hey|greetings': 'Hello! Welcome to our AI assistant. How can I help you today?',
            r'how are you|how\'?s it going|how do you do': 'I\'m doing great, thank you for asking! I\'m here to assist you. How can I help?',
            r'what.*your.*name|who are you': 'I\'m a rule-based chatbot created for the CODSOFT AI internship. You can call me ChatBot!',
            r'what can you do|capabilities|help': 'I can answer questions about AI, help with greetings, answer trivia, and provide general information.',
            r'what is ai|define ai|ai meaning': 'AI (Artificial Intelligence) is the simulation of human intelligence by machines, especially computer systems. It includes learning, reasoning, and problem-solving.',
            r'what is machine learning|define ml|ml meaning': 'Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.',
            r'what is deep learning|define dl': 'Deep Learning is a subset of Machine Learning using neural networks with multiple layers to process data.',
            r'tell me a joke|make me laugh|funny': 'Why did the AI go to school? To improve its learning model! 😄',
            r'current time|what time is it|tell me the time': f'The current time is {datetime.now().strftime("%H:%M:%S")}',
            r'thank you|thanks|appreciate|thank': 'You\'re welcome! Happy to help. Is there anything else you\'d like to know?',
            r'bye|goodbye|see you|exit|quit': 'Goodbye! Have a great day. Feel free to come back anytime!',
            r'what is chatbot|define chatbot': 'A chatbot is a software application that simulates conversation with users through text or voice interactions.',
            r'who created you|who made you|your creator': 'I was created by Siva Durga as part of the CODSOFT AI internship program.',
            r'what is your purpose|why do you exist': 'My purpose is to demonstrate rule-based chatbot design and to assist users with their queries.',
        }
        
        # Fallback responses for unmatched queries
        self.fallback_responses = [
            "I\'m not sure how to respond to that. Could you rephrase your question?",
            "That\'s an interesting question! Can you provide more details?",
            "I don\'t have information about that. Try asking me something else!",
            "I\'m still learning. Can you ask something I might know better?",
        ]
        
        self.fallback_index = 0
    
    def get_response(self, user_input):
        """Generate a response based on user input using pattern matching.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The chatbot's response
        """
        # Convert input to lowercase for case-insensitive matching
        user_input = user_input.lower().strip()
        
        # Check each rule against the user input
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return response
        
        # Return fallback response if no pattern matches
        fallback = self.fallback_responses[self.fallback_index]
        self.fallback_index = (self.fallback_index + 1) % len(self.fallback_responses)
        return fallback

# Initialize chatbot
chatbot = RuleBasedChatbot()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify API is running."""
    return jsonify({'status': 'API is running', 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint that processes user messages and returns responses.
    
    Request JSON:
        {"message": "user's message"}
        
    Response JSON:
        {"response": "bot's response", "timestamp": "timestamp"}
    """
    try:
        # Extract message from request
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        # Validate message
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        if len(user_message) > 1000:
            return jsonify({'error': 'Message is too long (max 1000 characters)'}), 400
        
        # Get bot response
        bot_response = chatbot.get_response(user_message)
        
        # Return response with metadata
        return jsonify({
            'response': bot_response,
            'user_message': user_message,
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

@app.route('/api/info', methods=['GET'])
def get_info():
    """Get information about the chatbot."""
    return jsonify({
        'name': 'Rule-Based Chatbot',
        'version': '1.0.0',
        'description': 'A chatbot that responds to user queries using pattern matching',
        'creator': 'Siva Durga',
        'organization': 'CODSOFT AI Internship',
        'total_rules': len(chatbot.rules),
        'timestamp': datetime.now().isoformat()
    }), 200

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found', 'status': 'error'}), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error', 'status': 'error'}), 500

if __name__ == '__main__':
    # Run the Flask application
    # Set debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5000)
