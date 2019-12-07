from app.route.stories.provider import Provider
from app.api.base import base_name as names
from app.api.helper import get_id_user_by_profile, get_id_user_by_profiles


def publicate_storie(args):
    """
    Опубликовать исторю
    :param args:
    :return:
    """
    provider = Provider()
    if isinstance(args.get(names.ID_PROFILE), list):
        id_users = get_id_user_by_profiles(args)
    else:
        id_users = get_id_user_by_profile(args)
    for id_user in id_users:
        args[names.ID_USER] = id_user.get(names.ID_USER)
        provider.publicate_storie(args)
    return names.OK


def insert_stories(args):
    """
    Создать историю
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.insert_stories(args)[0]
    args[names.ID_STORIES] = answer.get(names.ID_STORIES)
    args[names.POSITION] = 0
    for i in range(len(args.get(names.URL))):
        args[names.URL] = args.get(names.URL)[i]
        args[names.DESCRIPTION] = args.get(names.DESCRIPTION)[i] if args.get(names.DESCRIPTION) else ''
        provider.insert_image(args)
        args[names.POSITION] += 1
    return names.OK


def stories_profile(args):
    """
    Получить истории для профиля
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.stories_profile(args)
    return answer


def update_stories(args):
    """
    Обновить историю
    :param args:
    :return:
    """
    provider = Provider()
    provider.update_stories(args)
    provider.delete_images(args)
    args[names.POSITION] = 0
    for i in range(len(args.get(names.URL))):
        args[names.URL] = args.get(names.URL)[i]
        args[names.DESCRIPTION] = args.get(names.DESCRIPTION)[i]
        provider.insert_image(args)
        args[names.POSITION] += 1
    return names.OK


def change_status(args):
    """
    Изменить статус в действий пользователя
    :param args:
    :return:
    """
    provider = Provider()
    status = provider.select_status(args)
    args[names.IS_OPEN] = args[names.STATUS] == 'open'
    args[names.IS_VIEW] = args[names.STATUS] == 'view'
    if args.get(names.ID_NOTIFICATION) is not None:
        args[names.ACTIVE] = False if args[names.IS_VIEW] else True
        provider.update_notifications_user(args)
    if args.get(names.STATUS) is not None:
        if status:
            provider.update_status(args)
        else:
            provider.insert_status(args)
    if args.get(names.IS_LIKE):
        provider.update_like(args)
    return names.OK


def get_stories_list(args):
    """
    Поулчить истории для пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_stories_list(args)
    return answer


def get_all_stories(args):
    """
    Получить все истории для пнаели админа
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_all_stories(args)
    return answer
