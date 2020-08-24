from ..service import office_service, department_service
import copy


class ExpandService:

    @staticmethod
    def office(item):
        if item is None or 'office' not in item or item['office'] is None:
            return None

        item['office'] = office_service.get(item['office'])
        return item['office']

    @staticmethod
    def department(item):
        if item is None or 'department' not in item or item['department'] is None:
            return None

        item['department'] = department_service.get(item['department'])
        return item['department']

    @staticmethod
    def superdepartment(item):
        if item is None or 'superdepartment' not in item or item['superdepartment'] is None:
            return None

        item['superdepartment'] = department_service.get(item['superdepartment'])
        return item['superdepartment']

    def manager(self, item):
        if item is None or 'manager' not in item or item['manager'] is None:
            return None

        item['manager'] = copy.copy(self.managers.get(item['manager']))
        return item['manager']
