from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> This is Home</h1>"


if __name__ == "__main__":
    app.run(debug=True)
