import json
import copy
from os.path import join
from ..utils.pathutils import get_resources_path

items = {}
with open(join(get_resources_path(), "offices.json"), 'r') as json_file:
    json_data = json.load(json_file)
    for data in json_data:
        items[data['id']] = data


def get(office_id: int):
    """
        Returns the office by it's id

        Args:
            office_id (int): Unique identifier of the office

        Returns:
            dict: Return the representation of the office
        """
    return copy.copy(items.get(office_id))

