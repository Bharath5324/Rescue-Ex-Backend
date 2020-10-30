from flask import jsonify, Blueprint, current_app
from flask_restful import Api, Resource

API_APP = Blueprint(__name__, 'api_app')

API = Api(API_APP)

class ApiStatus(Resource):
	def get(self):
		return jsonify({'status': 'live',
		                'config': current_app.config['ENV'],
		                'version': '0.2.0'})

API.add_resource(ApiStatus, '/')