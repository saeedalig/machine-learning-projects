
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Starting Machine Learning Project"

if __name__ == "__main__":
    app.run(debug=True)