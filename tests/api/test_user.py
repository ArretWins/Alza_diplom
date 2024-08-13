from services.user_service import UserService


def test_create_with_array():
    users = UserService()
    response = users.create_user_with_array('ioioioio', 'Artem', "Wins",
                                            'aaa@aa.ru', '12313', '21313124')
    assert response['message'] == 'ok'


def test_login():
    users = UserService()
    response = users.login_user('ioioioio', '12313')

    assert response['code'] == 200


def test_update_user():
    users = UserService()
    response = users.update_user('ioioioio',
                                 'Wins', 'Wiins', "Wiiins",
                                 'Wins@aa.ru', '12313', '21313124')
    assert response['code'] == 200
