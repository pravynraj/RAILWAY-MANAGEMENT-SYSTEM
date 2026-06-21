FLASK_APP=run.py
FLASK_ENV=development
def create_app():
    app = Flask(__name__)
    return app
@app.route('/home')
def home():
    return "Hello"
def create_app():
    app = Flask(__name__)
    return app
@app.route("/")
def home():
    return "Hello World"
