import requests
import os
import logging

logger = logging.getLogger(__name__)


def get_employees(limit: int = 100, offset: int = 0, employee_ids: list = []):
    url = os.getenv('EMPLOYEE_URL')

    params = {}
    if limit is not None:
        params['limit'] = limit
    if offset is not None:
        params['offset'] = offset
    if employee_ids:
        for employee_id in employee_ids:
            params['id'] = employee_id

    try:
        response = requests.get(
            url=url,
            params=params)
        if response.ok:
            return response.json()
        else:
            return []
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        logger.error('Calling the employee service fail by time out')
        return []
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        logger.error('Calling the employee service fail by too many redirects')
        return []
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        logger.error('Calling the employee service fail by a service exception')
        return []
