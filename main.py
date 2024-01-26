from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.info("Received request for hello_world")
    return 'Hello, World!'
