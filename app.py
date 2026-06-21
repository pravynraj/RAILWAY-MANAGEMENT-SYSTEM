from flask import Flask

app = Flask(__RAILWAY-MANAGEMENT-SYSTEM__)

@app.route("/")
def home():
    return "Deployment successful"
    
