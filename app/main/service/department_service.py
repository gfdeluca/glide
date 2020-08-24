import json
import copy
from os.path import join
from ..utils.pathutils import get_resources_path

items = {}
with open(join(get_resources_path(), "departments.json"), 'r') as json_file:
    json_data = json.load(json_file)
    for data in json_data:
        items[data['id']] = data


def get(department_id: int) -> dict:
    """
    Returns the department by it's id

    Args:
        department_id (int): Unique identifier of the department

    Returns:
        dict: Return the representation of the department
    """
    return copy.copy(items.get(department_id))
