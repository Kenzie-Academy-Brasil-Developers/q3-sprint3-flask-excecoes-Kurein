from json import dump, load, JSONDecodeError
from app.exc.exception import error

def get_user_list():
    try:
        with open('app/database/database.json', 'r') as file:
            return load(file)
    except (FileNotFoundError, JSONDecodeError):
        return []

def create_user(user_info):
    users_list = get_user_list()
    user_info['id'] = len(users_list) +1

    if len(users_list) > 2:
        raise error

    users_list.append(user_info)
    with open ('app/database/database.json', 'w') as file:
        dump(users_list, file, indent=2)

    return {'msg': 'perfil criado com sucesso!'}