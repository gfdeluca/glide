from copy import deepcopy
from unittest.mock import Mock
from app.test.base import BaseTestCase
import app.main.service.employee_service as service


class ServiceEmployeeTestCase(BaseTestCase):
    single_connector_value = [{
        "id": 1,
        "first": "Patricia",
        "last": "Diaz",
        "department": 5,
        "office": 2,
        "manager": None
    }]

    single_connector_value_2 = [{
            "id": 2,
            "first": "Daniel",
            "last": "Smith",
            "department": 5,
            "office": 2,
            "manager": 1
        }]

    multiple_connector_value = [{
            "id": 1,
            "first": "Patricia",
            "last": "Diaz",
            "department": 5,
            "office": 2,
            "manager": None
        },
        {
            "id": 2,
            "first": "Daniel",
            "last": "Smith",
            "department": 5,
            "office": 2,
            "manager": 1
        }]

    def test_get_employees_without_expands(self):
        service.get_employees = Mock(return_value=deepcopy(self.single_connector_value))
        data = service.get_all_employees(10, 10, *[])
        self.assertCountEqual(data, self.single_connector_value)
        self.assertEqual(data[0]['first'], 'Patricia')
        self.assertEqual(data[0]['last'], 'Diaz')
        self.assertEqual(data[0]['department'], 5)
        self.assertEqual(data[0]['office'], 2)
        self.assertEqual(data[0]['manager'], None)
        self.assertEqual(service.get_employees.call_count, 1)

    def test_get_employees_with_expand_office(self):
        service.get_employees = Mock(return_value=deepcopy(self.single_connector_value))
        data = service.get_all_employees(10, 10, *['office'])
        self.assertNotIsInstance(data[0]['office'], int)
        self.assertEqual(data[0]['office']['id'], 2)
        self.assertEqual(data[0]['office']['city'], 'New York')
        self.assertEqual(data[0]['office']['country'], 'United States')
        self.assertEqual(data[0]['office']['address'], '20 W 34th St')

    def test_get_employees_with_chained_expands_and_null_manager(self):
        service.get_employees = Mock(return_value=deepcopy(self.single_connector_value))
        data = service.get_all_employees(10, 10, *['office', 'manager.office'])
        self.assertNotIsInstance(data[0]['office'], int)
        self.assertNotIsInstance(data[0]['manager'], int)
        self.assertEqual(data[0]['office']['id'], 2)
        self.assertEqual(data[0]['office']['city'], 'New York')
        self.assertEqual(data[0]['office']['country'], 'United States')
        self.assertEqual(data[0]['office']['address'], '20 W 34th St')
        self.assertEqual(data[0]['manager'], None)

        self.assertNotIsInstance(data[0]['manager'], int)
        self.assertEqual(service.get_employees.call_count, 2)

    def test_two_employees_with_chained_expands(self):
        service.get_employees = Mock(return_value=deepcopy(self.multiple_connector_value))
        data = service.get_all_employees(10, 10, *['department.superdepartment'])
        self.assertEqual(len(data), 2)
        self.assertNotIsInstance(data[0]['department'], int)
        self.assertNotIsInstance(data[0]['department']['superdepartment'], int)
        self.assertIsInstance(data[0]['office'], int)
        self.assertEqual(data[0]['manager'], None)

    def test_get_a_employee_without_expand(self):
        service.get_employees = Mock(return_value=deepcopy(self.single_connector_value))
        data = service.get_a_employee(1, *[])
        self.assertEqual(data['first'], 'Patricia')
        self.assertEqual(data['last'], 'Diaz')
        self.assertEqual(data['department'], 5)
        self.assertEqual(data['office'], 2)
        self.assertEqual(data['manager'], None)
        self.assertEqual(service.get_employees.call_count, 1)

    def test_get_a_employee_with_expand(self):
        service.get_employees = Mock(return_value=deepcopy(self.single_connector_value_2))
        service.get_employees.side_effect = [self.single_connector_value_2, self.single_connector_value]
        data = service.get_a_employee(1, *['manager'])
        self.assertEqual(data['first'], 'Daniel')
        self.assertEqual(data['last'], 'Smith')
        self.assertEqual(data['department'], 5)
        self.assertEqual(data['office'], 2)
        self.assertNotIsInstance(data['manager'], int)
        self.assertEqual(data['manager']['id'], 1)
        self.assertEqual(data['manager']['first'], 'Patricia')
        self.assertEqual(service.get_employees.call_count, 2)


class ServiceOfficeTestCase(BaseTestCase):
    """TODO: Create unit testing"""
    pass


class ServiceDepartmentTestCase(BaseTestCase):
    """TODO: Create unit testing"""
    pass


class ServiceExpandTestCase(BaseTestCase):
    """TODO: Create unit testing"""
    pass
