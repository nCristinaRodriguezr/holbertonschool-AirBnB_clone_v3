#!/usr/bin/python3
"""
organize and structure the code of a Flask application that uses API versions
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

import api.v1.views.index