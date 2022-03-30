# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route("/")
def index():
    return f"<p>This returns the value of the index function<p>"


@app.route("/info")
def info():
    return f"<p>This returns everything of the info page.<p>"

if __name__ == "__main__":
    app.run()