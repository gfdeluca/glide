from flask_restx import Namespace, fields


class EmployeeApi:
    api = Namespace('employee', description='Employee of the company')
    employee = api.model('employee', {
        'id': fields.Integer(required=True, description='Id of the employee'),
        'first': fields.String(required=True, description='First name of the person'),
        'last': fields.String(required=True, description='Surname of the person'),
        'department': fields.Raw(description='Id or object of the department where the employee belongs'),
        'office': fields.Raw(description='Id or object of the office where the employee belongs'),
        'manager': fields.Raw(description='Id or object of the manager of the employee')
    })
