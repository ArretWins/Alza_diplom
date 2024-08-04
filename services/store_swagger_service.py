from services.base_service import BaseService


class StoreService(BaseService):

    def __init__(self):
        super().__init__()
        # self.url = 'https://petstore.swagger.io/#/pet/addPet'
        self.url = 'https://petstore.swagger.io/v2/store/order'

    def delete_order_by_id(self, order_id):
        url = f'{self.url}/{order_id}'
        return self.delete_request(url=url)
