from ..connector.employee_connector import get_employees
from functools import reduce
from ..service.expand_service import ExpandService


def get_all_employees(limit: int, offset: int, *expanse_functions) -> list:
    employees: list = get_employees(limit=limit, offset=offset)
    expand_employees(employees, *expanse_functions)

    return employees


def get_a_employee(employee_id, *expanse_functions):
    employee = get_employees(limit=None, offset=None, employee_ids=[employee_id])
    expand_employees(employee, *expanse_functions)

    return employee[0] if employee else None


def expand_employees(employees, *args) -> list:
    if len(args) == 0:
        return employees

    has_manager = False
    expand_service = ExpandService()
    expand_functions = []
    for arg in args:
        if 'manager' in arg:
            has_manager = True

        lst_func = [getattr(expand_service, func) for func in reversed(arg.split('.'))]
        expand_functions.append(compose_function(*lst_func))

    if has_manager:
        managers_id = {emp['manager'] for emp in employees}
        managers = get_all_employees(len(managers_id), 0)
        managers = {emp['id']: emp for emp in managers}
        expand_service.managers = managers

    for employee in employees:
        for expand_function in expand_functions:
            expand_function(employee)

    return employees


def compose_function(*func):
    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)
