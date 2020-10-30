from flask import Blueprint

WEBAPP =Blueprint(__name__, 'webapp', template_folder='templates',\
                    static_url_path='/static', static_folder='static')

from . import routes