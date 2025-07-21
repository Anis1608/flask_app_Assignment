from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route('/api')
def get_data():
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            return jsonify({"error": "Data file not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
