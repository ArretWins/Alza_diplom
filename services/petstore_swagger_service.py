from services.base_service import BaseService
import allure


class PetStoreService(BaseService):

    def __init__(self):
        super().__init__()
        # self.url = 'https://petstore.swagger.io/#/pet/addPet'
        self.url = 'https://petstore.swagger.io/v2/pet'

    def add_pet(self, pet):
        with allure.step('Add pet'):
            body = {
                "id": 0,
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
