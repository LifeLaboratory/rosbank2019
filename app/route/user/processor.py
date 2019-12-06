from app.route.user.provider import Provider


def auth(user_data):
    provider = Provider()
    answer = provider.auth_user(user_data)
    if isinstance(answer, list):
        answer = answer[0]
    return answer


def register(user_data):
    provider = Provider()
    check = provider.check_user(user_data)
    id_user = None
    if not check:
        id_user = provider.register_user(user_data)
        if isinstance(id_user, list):
            id_user = id_user[0]
    else:
        print('Пользователь существует', user_data)
    return id_user
