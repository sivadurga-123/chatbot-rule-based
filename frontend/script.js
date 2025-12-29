// Configuration
const API_BASE_URL = 'http://localhost:5000';

// DOM Elements
const chatMessagesEl = document.getElementById('chatMessages');
const userInputEl = document.getElementById('userInput');
const chatFormEl = document.getElementById('chatForm');

// Event Listeners
chatFormEl.addEventListener('submit', handleSendMessage);
userInputEl.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSendMessage(e);
    }
});

// Send message function
async function handleSendMessage(e) {
    e.preventDefault();
    
    const message = userInputEl.value.trim();
    if (!message) return;
    
    // Clear input
    userInputEl.value = '';
    userInputEl.focus();
    
    // Display user message
    addMessage(message, 'user');
    
    // Show loading indicator
    const loadingMsg = addMessage('Thinking...', 'bot');
    loadingMsg.style.opacity = '0.7';
    
    try {
        // Send request to backend
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Remove loading message
        chatMessagesEl.removeChild(loadingMsg.parentElement);
        
        // Display bot response
        if (data.response) {
            addMessage(data.response, 'bot');
        } else {
            addMessage('Sorry, I couldn\'t process your message. Please try again.', 'bot');
        }
    } catch (error) {
        console.error('Error:', error);
        
        // Remove loading message
        if (loadingMsg.parentElement) {
            chatMessagesEl.removeChild(loadingMsg.parentElement);
        }
        
        // Show error message
        addMessage('Connection error! Make sure the backend is running on http://localhost:5000', 'bot');
    }
}

// Add message to chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    const textP = document.createElement('p');
    textP.textContent = text;
    contentDiv.appendChild(textP);
    
    messageDiv.appendChild(contentDiv);
    
    // Add timestamp
    const timeSpan = document.createElement('span');
    timeSpan.className = 'message-time';
    timeSpan.textContent = getCurrentTime();
    messageDiv.appendChild(timeSpan);
    
    chatMessagesEl.appendChild(messageDiv);
    
    // Auto scroll to bottom
    chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;
    
    return contentDiv;
}

// Get current time in HH:MM format
function getCurrentTime() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    return `${hours}:${minutes}`;
}

// Send suggestion
function sendSuggestion(text) {
    userInputEl.value = text;
    userInputEl.focus();
    chatFormEl.dispatchEvent(new Event('submit'));
}

// Initialize
console.log('Chatbot loaded successfully!');
console.log(`Connecting to backend at: ${API_BASE_URL}`);

// Optional: Test connection on load
window.addEventListener('load', () => {
    console.log('Page fully loaded. Chat is ready to use.');
});
