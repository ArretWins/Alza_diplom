from services.base_service import BaseService
import allure


class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/user'

    def create_user_with_array(self, username, first_name, last_name, email, password, phone_number):
        with allure.step('Create a new user'):
            url = f'{self.url}/createWithArray'
            body = [
                {
                    "id": 0,
                    "username": username,
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "password": password,
                    "phone": phone_number,
                    "userStatus": 0
                }
            ]
            return self.post_request(url=url, body=body)

    def login_user(self, username, password):
        with allure.step('Login user'):
            url = f'{self.url}/login?username={username}&password={password}'
            return self.get_request(url=url)

    def get_user_by_username(self, username):
        with allure.step('Get user by id'):
            url = f'{self.url}/{username}'
            return self.get_request(url=url)

    def delete_user(self, username):
        with allure.step('Delete user'):
            url = f'{self.url}/{username}'
            return self.delete_request(url=url, code=200)

    def update_user(self, old_username, username, first_name, last_name, email, password, phone_number):
        with allure.step('Update user'):
            url = f'{self.url}/{old_username}'
            body = {
                    "id": 0,
                    "username": username,
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "password": password,
                    "phone": phone_number,
                    "userStatus": 0
                }

            return self.put_request(url=url, body=body)