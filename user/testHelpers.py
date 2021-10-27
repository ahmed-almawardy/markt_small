from user.models import User

USER_DATA = {
    'username':'user',
    'first_name': 'first',
    'last_name': 'last',
    'email': 'username@email.com',
    'password': 'A12345678user',
    'confirm_password': 'A12345678user',
}

NEW_DATA = {
    'username':'userA',
    'first_name': 'firSst',
    'last_name': 'last',
    'email': 'Username@email.com',
    'password': '1S23456a',
    'confirm_password': '1S23456a',

}

USER_DATA_CREATE = {
    'username':'user1',
    'first_name': 'first',
    'last_name': 'last',
    'email': 'username1@email.com',
    'password': 'A12345678user',
}


def create_user(**update):
    data = USER_DATA_CREATE.copy()
    if update:
        data.update(update)
    return User.objects.create(**data)
