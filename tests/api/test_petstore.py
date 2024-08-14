from services.petstore_swagger_service import PetStoreService


def test_add_pet():
    petstore = PetStoreService()
    response = petstore.add_pet('Pig')
    assert response['name'] == 'Pig'


# def test_get_pet_by_id():
#     petstore = PetStoreService()
#     response = petstore.get_pet_by_id(1)
#     assert response['name'] == 'sophie'
