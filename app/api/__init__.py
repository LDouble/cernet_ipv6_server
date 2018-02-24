from flask import Blueprint

api = Blueprint("api",__name__)
api_1 = Blueprint("api_1.0", __name__)

from .authentication import auth
from . import view
from . import API_1
