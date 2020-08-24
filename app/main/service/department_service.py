import json
import copy
from os.path import join
from ..utils.pathutils import get_resources_path

items = {}
with open(join(get_resources_path(), "departments.json"), 'r') as json_file:
    json_data = json.load(json_file)
    for data in json_data:
        items[data['id']] = data


def get(department_id: int):
    return copy.copy(items.get(department_id))
