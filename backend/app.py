from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            r'hello|hi|hey|greetings': 'Hello! How can I help you today?',
            r'how are you|whats up': 'I\'m doing great, thanks for asking! How are you?',
            r'what.*your name|who are you': 'I\'m a rule-based chatbot created for CODSOFT internship.',
            r'what can you do': 'I can answer greetings, questions about myself, and provide general information.',
            r'bye|goodbye|see you|exit': 'Goodbye! Have a great day!',
            r'thank you|thanks|appreciate': 'You\'re welcome! Happy to help!',
            r'what is ai|define ai': 'AI (Artificial Intelligence) is the simulation of human intelligence by machines.',
            r'what is chatbot': 'A chatbot is a software that simulates conversation with users.',
            r'time': 'I don\'t have real-time access, but you can check your device\'s clock.',
            r'who created you|who made you': 'I was created as part of the CODSOFT AI internship program.',
            r'tell me a joke': 'Why did the AI go to school? To improve its learning model! 😄',
            r'help': 'I can help you with various questions! Try asking me things like: hello, how are you, what is AI, or tell me a joke!',
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        if not user_input:
            return "Please enter a message!"
        
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input):
                return response
        
        return "I'm not sure how to respond to that. Could you try rephrasing? Or type 'help' for suggestions."

chatbot = RuleBasedChatbot()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Chatbot API is running! Send POST requests to /chat'})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = chatbot.get_response(user_message)
        return jsonify({'response': response, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
