from flask import Flask
from flask_cors import CORS
app = Flask(__name__)\

CORS(app)

@app.route("/hello")
def get():
    return "hello"

@app.route("/", methods=['GET'])
app.run()