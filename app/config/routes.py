from flask import Blueprint
from flask_restful import Api

from app.resources.cat import CatResource, CatListResource

routes_bp = Blueprint('routes', __name__)
api = Api(routes_bp)

api.add_resource(CatResource, '/cat', endpoint='cat', methods=['POST'])
api.add_resource(CatResource, '/cat/<int:cat_id>', endpoint='cat_by_id', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(CatListResource, '/cat_list', endpoint='cat_list')
