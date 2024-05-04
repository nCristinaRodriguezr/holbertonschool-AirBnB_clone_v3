#!/usr/bin/python3
"""
define a route in the API that can be accessed via the /status URL
and that returns a JSON indicating that the API status is "OK".
"""
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def get_status():
    return {"status": "OK"}
