from flask import Flask

app = Flask(__RAILWAY-MANAGEMENT-SYSTEM__)

@app.route("/")
def home():
    return "Deployment successful"
    @app.route("/")
def home():
    return "Hello World"


@app.route("/login")
def login():
    return "Login page"
    
