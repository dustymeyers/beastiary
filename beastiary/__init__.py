from flask import Blueprint

bp = Blueprint('bestiary', __name__, url_prefix='/api/bestiary')

from . import routes
