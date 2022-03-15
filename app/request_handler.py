from json import dump, load, JSONDecodeError
from app.exc.emailError import emailError
from app.exc.nameOrMailInvalid import nameOrMailInvalid

def get_user_list():
    try:
        with open('app/database/database.json', 'r') as file:
            return load(file)
    except (FileNotFoundError, JSONDecodeError):
        return []

def create_user(user_info):
    if not type(user_info['nome']) == str or not type(user_info['email']) == str:
        raise nameOrMailInvalid

    users_list = get_user_list()
    user_info['nome'] = user_info['nome'].title()
    user_info['email'] = user_info['email'].lower()
    if users_list == []:
        user_info['id'] = 1
    else:
        user_info['id'] = users_list[-1]["id"]+1

    for user in users_list:
        if user['email'] == user_info['email']:
            raise emailError

    users_list.append(user_info)
    with open ('app/database/database.json', 'w') as file:
        dump(users_list, file, indent=2)

    return user_info