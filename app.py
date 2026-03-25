from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary storage (like a mini database)
messages = []

# GET - Frontend fetches all messages


@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

# POST - Frontend sends a new message


@app.route('/api/messages', methods=['POST'])
def add_message():
    data = request.json               # Get data from frontend
    name = data['name']
    message = data['message']
    messages.append({'name': name, 'message': message})
    return jsonify({'status': 'saved!'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
