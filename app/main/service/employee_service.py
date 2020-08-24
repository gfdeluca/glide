from ..connector.employee_connector import get_employees
from functools import reduce
from ..service.expand_service import ExpandService


def get_all_employees(limit: int, offset: int, *expanse_functions: list) -> list:
    """
    Service for gathering all employees from a external service given its limit and offset, also transform the response
    with the specified extensions.

    Args:
        limit (int): Determinate the max amount of employee to be returned
        offset (int): Index at which to start.
        *expanse_functions (list): Array of instructions to apply to the returned data 

    Returns:
        list: Array with all the employees with it data transformed

    """
    employees: list = get_employees(limit=limit, offset=offset)
    expand_employees(employees, *expanse_functions)

    return employees


def get_a_employee(employee_id: int, *expanse_functions: list) -> dict:
    """
    Service to get a specific employee from a external service given its id, also transform the response with the
    specified extensions.
    Args:
        employee_id (int): Unique identifier of the employee
        *expanse_functions (list): Array of instructions to apply to the returned data

    Returns:
        dict: Representation of the employee information
    """
    employee = get_employees(limit=None, offset=None, employee_ids=[employee_id])
    expand_employees(employee, *expanse_functions)

    return employee[0] if employee else None


def expand_employees(employees: list, *args: list) -> list:
    """
    Function that receives all the employees to transform it's information determined.
    Args:
        employees (list): List of employees to be transformed
        *args: List of transformations to be executed to the employees

    Returns:
        list: List of employees transformed
    """
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
    """
    Compose two or more functions to transform the response of each.

    Args:
        *func: List of functions to be executed

    Returns:
        lambda: Lambda function with the compose of functions
    """
    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)
