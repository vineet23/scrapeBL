from flask import Flask
from flask import jsonify
from scraping import scrape

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(Cars=scrape())


if __name__ == "__main__":
    app.run(debug=True, host='10.0.40.147', port=5001)