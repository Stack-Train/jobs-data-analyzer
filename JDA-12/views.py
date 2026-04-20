import os
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

DATA_API_URL = os.getenv('DATA_API_URL', 'http://localhost:4000')


@bp.route('/hello')
def hello():
    return {'hello': 'world'}


@bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", data_api_url=DATA_API_URL)


@bp.route("/", methods=['GET'])
def index():
    return render_template("index.html")
