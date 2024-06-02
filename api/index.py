# api/index.py
from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route('/fast', methods=['GET', 'POST'])
def fast_response():
    return jsonify({"message": "Fast response"}), 200

@app.route('/slow', methods=['GET', 'POST'])
def slow_response():
    time.sleep(random.uniform(1, 3))  # Simulate slow response
    return jsonify({"message": "Slow response"}), 200

api_endpoints = {
    'REST': ['/fast', '/slow'],
    'large_payload': ['/slow']
}

if __name__ == '__main__':
    app.run(port=5000)
