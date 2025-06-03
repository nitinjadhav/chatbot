from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '')
    
    # Dummy bot response
    bot_reply = f"You said: {user_msg}"
    
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
