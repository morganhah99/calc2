"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.azure_controller import AzureController
from app.controllers.git_controller import GitController
from app.controllers.glossary_controller import GlossaryController
from app.controllers.vi_controller import ViController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/azure", methods=['GET'])
def azure_get():
    return AzureController.get()

@app.route("/git", methods=['GET'])
def git_get():
    return GitController.get()

@app.route("/vi", methods=['GET'])
def vi_get():
    return ViController.get()

@app.route("/glossary", methods=['GET'])
def glossary_get():
    return GlossaryController.get()
