from services.base_service import BaseService
import allure


class StoreService(BaseService):

    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/store/order'

    def add_order_by_id(self, order_id, pet_id):
        with allure.step('Add order'):
            body = {
                "id": order_id,
                "petId": pet_id,
                "quantity": 0,
                "shipDate": "2024-08-15T14:12:06.158Z",
                "status": "placed",
                "complete": "true"
            }
            url = self.url
            return self.post_request(url=url, body=body)

    def get_order_by_id(self, order_id):
        with allure.step('Get order by id'):
            url = f'{self.url}/{order_id}'
            return self.get_request(url=url)

    def delete_order_by_id(self, order_id):
        with allure.step('Delete order by id'):
            url = f'{self.url}/{order_id}'
            return self.delete_request(url=url, code=200)
