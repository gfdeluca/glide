import unittest

import json
from app.test.base import BaseTestCase


def get_employees(self):
    return self.client.get('/employee?limit=5&offset=0&expand=manager.office')


def get_employee(self):
    return self.client.get(
        '/employee/1?expand=manager.office'
    )


def get_employee_not_found(self):
    return self.client.get(
        '/employee/A'
    )


class IntegrationTest(BaseTestCase):
    def test_list_employees(self):
        """ Test for listing employee with a expanse """
        with self.client:
            response = get_employees(self)
            self.assert200(response)
            self.assertTrue(response.content_type == 'application/json')

            data = json.loads(response.data.decode())
            self.assertTrue(len(data['employees']) == 5)

    def test_get_employees(self):
        """ Test for getting a specific employee with a expanse """
        with self.client:
            response = get_employee(self)
            self.assert200(response)
            self.assertTrue(response.content_type == 'application/json')

            data = json.loads(response.data.decode())
            self.assertTrue('employees' is not data)

    def test_no_employee_found(self):
        with self.client:
            response = get_employee_not_found(self)
            self.assert200(response)
            data = json.loads(response.data.decode())
            self.assertEqual(data['code'], 404)
            self.assertEqual(data['description'], 'The employee of the search is not in out database')


if __name__ == '__main__':
    unittest.main()
