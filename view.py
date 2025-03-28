from flask import Flask, jsonify, render_template
import random
import string
from datetime import datetime, timedelta

app = Flask(__name__)

def generate_random_data():
    """Generates a dictionary with random data."""
    return {
        "random_number": random.randint(1, 100),
        "random_string": ''.join(random.choices(string.ascii_letters, k=10)),
        "random_date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "random_float": round(random.uniform(1, 100), 2),
    }

@app.route("/")
def home():
    """Displays random data."""
    data = generate_random_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)
