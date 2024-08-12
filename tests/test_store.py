from services.store_swagger_service import StoreService


def test_delete():
    store = StoreService()
    response = store.delete_order_by_id(3)
    assert response['message'] == 'Order Not Found'
