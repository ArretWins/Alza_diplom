from services.base_service import BaseService


class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/user'

    def create_user_with_array(self, username, first_name, last_name, email, password, phone_number):
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
        url = f'{self.url}/login?username={username}&password={password}'
        return self.get_request(url=url)

    def update_user(self, old_username, username, first_name, last_name, email, password, phone_number):
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