from flask import Flask, render_template, jsonify
import os
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-even')
def generate_even():
    even_number = random.choice(range(0, 100, 2))
    return jsonify({'number': even_number})

@app.route('/generate-odd')
def generate_odd():
    odd_number = random.choice(range(1, 100, 2))
    return jsonify({'number': odd_number})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)
