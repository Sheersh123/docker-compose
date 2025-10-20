from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Flask behind Nginx! 🚀</h1>"

@app.route("/ping")
def ping():
    return {"pong": True}

@app.route("/hello")
def ping2():
    return {"msg": "hello-there"}

