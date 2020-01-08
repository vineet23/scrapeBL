from flask import Flask
from flask import jsonify
from scraping import scrape

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(Diet=scrape())

if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.104', port=5000)