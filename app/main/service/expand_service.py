from ..service import office_service, department_service
import copy


class ExpandService:

    @staticmethod
    def office(item: dict) -> dict:
        """
        Transformation function for the office expand
        Args:
            item (dict): Representation of the employee object

        Returns:
            dict: Representation of the office object that has be added
        """
        if item is None or 'office' not in item or item['office'] is None:
            return None

        item['office'] = office_service.get(item['office'])
        return item['office']

    @staticmethod
    def department(item: dict) -> dict:
        """
        Transformation function for the department expand
        Args:
            item (dict): Representation of the employee object

        Returns:
            dict: Representation of the department object that has be added
        """
        if item is None or 'department' not in item or item['department'] is None:
            return None

        item['department'] = department_service.get(item['department'])
        return item['department']

    @staticmethod
    def superdepartment(item: dict) -> dict:
        """
        Transformation function for the superdepartment expand
        Args:
            item (dict): Representation of the deparment object

        Returns:
            dict: Representation of the superdepartment object that has be added
        """
        if item is None or 'superdepartment' not in item or item['superdepartment'] is None:
            return None

        item['superdepartment'] = department_service.get(item['superdepartment'])
        return item['superdepartment']

    def manager(self, item: dict) -> dict:
        """
        Transformation function for the manager expand
        Args:
            item (dict): Representation of the employee object

        Returns:
            dict: Representation of the manager object that has be added
        """
        if item is None or 'manager' not in item or item['manager'] is None:
            return None

        item['manager'] = copy.copy(self.managers.get(item['manager']))
        return item['manager']
