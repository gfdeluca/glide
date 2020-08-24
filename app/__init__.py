from flask_restx import Api
from flask import Blueprint

from .main.controller.employee_controller import api as employee_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Glide exam',
          version='1.0',
          description=''
          )

api.add_namespace(employee_ns)
