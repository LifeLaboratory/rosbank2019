from app.route.profile.provider import Provider


def get_profile(args):
    """
    Получить профиль пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_profile(args)
    return answer


def update_profile(args):
    """
    Обновить профиль пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.update_profile(args)
    return answer
