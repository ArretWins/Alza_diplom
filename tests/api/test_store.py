from services.store_swagger_service import StoreService


def test_add_order_by_id():
    store = StoreService()
    order_id = 375
    pet_id = 3751
    response = store.add_order_by_id(order_id, pet_id)
    assert response['id'] == order_id
    assert response['petId'] == pet_id


def test_get_order_by_id():
    store = StoreService()
    order_id = 375
    response = store.get_order_by_id(order_id)
    assert response['id'] == order_id


def test_delete_order_by_id():
    store = StoreService()
    response = store.delete_order_by_id(375)
    assert response['code'] == 200, f"Expected code 200, but got {response['code']}"
    assert response['type'] == 'unknown', f"Expected type 'unknown', but got {response['type']}"
    assert response['message'] == '375', f"Expected message '375', but got {response['message']}"
