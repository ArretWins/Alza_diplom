from services.base_service import BaseService
import allure


class PetStoreService(BaseService):

    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/pet'

    def add_pet(self, pet_id, pet):
        with allure.step('Add pet'):
            body = {
                "id": pet_id,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": pet,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            }

            url = self.url
            return self.post_request(url=url, body=body)

    def get_pet_by_id(self, pet_id):
        with allure.step('Get pet by id'):
            url = f'{self.url}/{pet_id}'
            return self.get_request(url=url)

    def update_pet_by_id(self, pet_id, pet):
        with allure.step('Update pet by id'):
            url = f'{self.url}/{pet_id}'
            body = {
                "id": pet_id,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": pet,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            }

            return self.put_request(url=url, body=body)

    def delete_pet_by_id(self, pet_id):
        with allure.step('Delete pet by id'):
            url = f'{self.url}/{pet_id}'
            return self.delete_request(url=url, code=200)
