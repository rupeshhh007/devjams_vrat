from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data['name']
    email = data['email']
    message = data['message']

    # Store data in the database
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO responses (name, email, message) VALUES (?, ?, ?)',
                   (name, email, message))
    conn.commit()
    conn.close()

    return jsonify(success=True), 200

@app.route('/responses', methods=['GET'])
def view_responses():
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM responses')
    responses = cursor.fetchall()
    conn.close()
    return render_template('responses.html', responses=responses)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

