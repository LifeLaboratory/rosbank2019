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
        answer = provider.publicate_storie(args)
    return 'OK'


def insert_stories(args):
    """
    Создать историю
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.insert_stories(args)[0]
    args['id_stories'] = answer.get('id_stories')
    args['position'] = 0
    for image in args.get('url'):
        args['url'] = image
        provider.insert_image(args)
        args['position'] += 1
    return 'OK'


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
    answer = provider.update_stories(args)
    answer = provider.delete_images(args)
    args['position'] = 0
    for image in args.get('url'):
        args['url'] = image
        provider.insert_image(args)
        args['position'] += 1
    return 'OK'


def change_status(args):
    """
    Изменить статус в действий пользователя
    :param args:
    :return:
    """
    provider = Provider()
    status = provider.select_status(args)
    args['is_open'] = args['status'] == 'open'
    args['is_view'] = args['status'] == 'view'
    if args.get('id_notification') is not None:
        args['active'] = False if args['is_view'] else True
        answer = provider.update_notifications_user(args)
    if args.get('status') is not None:
        if status:
            answer = provider.update_status(args)
        else:
            answer = provider.insert_status(args)
    if args.get(names.IS_LIKE):
        answer = provider.update_like(args)
    return 'OK'


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
