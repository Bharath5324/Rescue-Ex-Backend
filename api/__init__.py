from flask import jsonify, Blueprint, current_app

API_APP = Blueprint(__name__, 'api_app')
WEBAPP =Blueprint(__name__, 'webapp', template_folder='templates',\
                    static_url_path='/static', static_folder='static')