from app.controllers.controller import ControllerBase
from flask import render_template

class GitController(ControllerBase):
    @staticmethod
    def get():
        return render_template('git.html')
