from services.user_service import UserService


def test_create_with_array():
    users = UserService()
    response = users.create_user_with_array('ioioioio', 'Bill', "Wins",
                                            'aaa@aa.com', '12313', '21313124')
    assert response['message'] == 'ok'


def test_get_user_by_username():
    users = UserService()
    username = 'ioioioio'
    first_name = 'Bill'
    response = users.get_user_by_username(username)
    assert response['username'] == username
    assert response['firstName'] == first_name


def test_login():
    users = UserService()
    response = users.login_user('ioioioio', '12313')
    assert response['code'] == 200


def test_update_user():
    users = UserService()
    response = users.update_user('ioioioio',
                                 'Wins', 'Wiins', "Wiiins",
                                 'Wins@aa.com', '12313', '21313124')
    assert response['code'] == 200


def test_delete_user():
    users = UserService()
    response = users.delete_user('ioioioio')
    assert response['code'] == 200, f"Expected code 200, but got {response['code']}"
    assert response['type'] == 'unknown', f"Expected type 'unknown', but got {response['type']}"
    assert response['message'] == 'ioioioio', f"Expected message '375', but got {response['message']}"
