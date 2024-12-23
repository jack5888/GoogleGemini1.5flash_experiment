from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot_functions import generate_chatbot_response


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
   user_input = request.get_json()['user_input']  # Get JSON data from request
   bot_response = generate_chatbot_response(user_input)
   return jsonify({'response': bot_response})


if __name__ == '__main__':
   app.run(debug=True)