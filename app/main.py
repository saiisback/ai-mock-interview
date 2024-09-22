from flask import Flask, request, jsonify
from flask_cors import CORS
from interview import start_interview

app = Flask(__name__)
CORS(app)

@app.route('/start-interview', methods=['POST'])
def start():
    data = request.json
    return jsonify(start_interview(data))

if __name__ == '__main__':
    app.run(debug=True)
