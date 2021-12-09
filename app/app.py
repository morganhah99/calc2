"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/home")
def home():
    """index home response"""
    return render_template('home.html')

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()