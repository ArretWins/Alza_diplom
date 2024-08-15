from services.petstore_swagger_service import PetStoreService


def test_add_pet():
    petstore = PetStoreService()
    response = petstore.add_pet(375, 'Martin')
    assert response['name'] == 'Martin'


def test_update_pet_by_id():
    petstore = PetStoreService()
    response = petstore.add_pet(375, 'Tommy')
    assert response['name'] == 'Tommy'


def test_get_pet_by_id():
    petstore = PetStoreService()
    response = petstore.get_pet_by_id(375)
    assert response['name'] == 'Tommy'


def test_delete_pet_by_id():
    petstore = PetStoreService()
    response = petstore.delete_pet_by_id(375)
    assert response['code'] == 200, f"Expected code 200, but got {response['code']}"
    assert response['type'] == 'unknown', f"Expected type 'unknown', but got {response['type']}"
    assert response['message'] == '375', f"Expected message '375', but got {response['message']}"
