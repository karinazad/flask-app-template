from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """
    Pass the value '/' to @app.route() to signify that this function will
    respond to web requests for the URL /, which is the main URL.
    """
    return 'Hello, World!'

