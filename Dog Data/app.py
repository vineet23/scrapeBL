from flask import Flask
from flask import jsonify
from scraping import scrape,imageDownload

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(Dogs=scrape())

@app.route('/img')
def indeximg():
    return imageDownload()


if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.111', port=5000)