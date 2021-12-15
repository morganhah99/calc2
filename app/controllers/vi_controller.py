from app.controllers.controller import ControllerBase
from flask import render_template

class ViController(ControllerBase):
    @staticmethod
    def get():
        return render_template('vi.html')