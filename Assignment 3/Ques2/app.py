from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import dotenv
import os
dotenv.load_dotenv() 
MONGO_URI = os.getenv("MONGO_URI")
app = Flask(__name__)

client = MongoClient(MONGO_URI)
db = client['mydatabase']
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        
        if not name or not password:
            error = "Name and Password are required."
            return render_template('index.html', error=error)

        try:
            collection.insert_one({'name': name, 'password': password})
            return redirect(url_for('success'))
        except Exception as e:
            error = f"Error: {str(e)}"
            return render_template('index.html', error=error)

    return render_template('index.html', error=None)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
