from flask_restx import Resource, abort
from flask import request
from ..api.apis import EmployeeApi
from ..service.employee_service import get_all_employees, get_a_employee
from ..model.error_models import NotFoundException
import dataclasses
import json

api = EmployeeApi.api
_api = EmployeeApi.employee


@api.route('')
@api.doc(
    params={
        'limit': {'description': 'Amount of items to return. Default 100', 'in': 'query', 'type': 'int'},
        'offset': {'description': 'Pagination of the set', 'in': 'query', 'type': 'int'},
        'expand': {'description': 'What field to expand', 'in': 'query', 'type': 'string'}
    }
)
class EmployeesList(Resource):
    @api.doc('List of employees')
    @api.marshal_list_with(_api, envelope='employees')
    def get(self):
        """
        Get a list of employees with its corresponding data if applied by the expand parameter

        Args:

        Returns:
            None
        """
        api.logger.info("Some log from the controller")
        expands = request.args.getlist("expand")
        limit = request.args.get("limit", type=int, default=100)
        if limit > 1000:
            limit = 1000

        offset = request.args.get("offset", type=int, default=0)
        employees: list = get_all_employees(limit, offset, *expands)
        return employees


@api.route('/<employee_id>')
@api.doc(
    params={
        'employee_id': {'description': 'identifier', 'in': 'path', 'type': 'int'},
        'expand': {'description': 'What field to expand', 'in': 'query', 'type': 'string'}
    }
)
@api.response(404, 'Employee not found.')
class EmployeeDetail(Resource):
    @api.doc('get a user')
    @api.marshal_with(_api)
    def get(self, employee_id: int):
        """Get a employee given its identifier,

        Args:
            employee_id (int): Unique identifier of the employee.

        Returns:
            object:
        """
        expands = request.args.getlist("expand")
        employee = get_a_employee(employee_id, *expands)

        if not employee:
            raise NotFoundException("Employee don't found", "The employee of the search is not in out database")
        else:
            return employee
