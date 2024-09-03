import json
import allure
import requests
from helpers.logger import create_logger


class BaseService:

    def __init__(self):
        self.logger = create_logger()

    def post_request(self, url, body, code=200):
        with allure.step("Post request"):
            headers = {
                'Content-Type': 'application/json',
                'accept': 'application/json'
            }
            payload = json.dumps(body)
            response = requests.post(url, data=payload, headers=headers)

            if response.status_code == code:
                self.logger.info(f'POST Request was successful: {response.url} -- {response.text}')
                return response.json()
            else:
                self.logger.error(f'POST Request failed: {response.url} -- {response.text}')
                return False

    def put_request(self, url, body, code=200):
        with allure.step("Put request"):
            headers = {
                'Content-Type': 'application/json',
                'accept': 'application/json'
            }
            payload = json.dumps(body)
            response = requests.put(url, data=payload, headers=headers)

            if response.status_code == code:
                self.logger.info(f'PUT Request was successful: {response.url} -- {response.text}')
                return response.json()
            else:
                self.logger.error(f'PUT Request failed: {response.url} -- {response.text}')
                return False

    def get_request(self, url, code=200):
        with allure.step("Get request"):
            headers = {
                'accept': 'application/json'
            }
            response = requests.get(url, headers=headers)

            if response.status_code == code:
                self.logger.info(f'GET Request was successful: {response.url} -- {response.text}')
                return response.json()
            else:
                self.logger.error(f'GET Request failed: {response.url} -- {response.text}')
                return False

    def delete_request(self, url, code=404):
        with allure.step("Delete request"):
            headers = {
                'accept': 'application/json'
            }
            response = requests.delete(url, headers=headers)

            if response.status_code == code:
                self.logger.info(f'DELETE Request was successful: {response.url} -- {response.text}')
                return response.json()
            else:
                self.logger.error(f'DELETE Request failed: {response.url} -- {response.text}')
                return False
