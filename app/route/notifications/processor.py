from app.route.notifications.provider import Provider
from app.route.stories.provider import Provider as provider_stories
from app.api.base import base_name as names
from app.api.helper import get_id_user_by_profile, get_admins_ids


def add_notification(args):
    """
    Добавить уведомление
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.insert_notification(args)[0]
    args[names.ID_NOTIFICATION] = answer.get(names.ID_NOTIFICATION)
    id_users = get_id_user_by_profile(args)
    for id_user in id_users:
        args[names.ID_USER] = id_user.get(names.ID_USER)
        provider.insert_notifications_users(args)
    return answer


def get_notification(args):
    """
    Получить список уведомлений для пользователя
    :param args:
    :return:
    """
    req_fields = [names.IMAGE, names.DESCRIPTION, names.TYPE]
    provider = Provider()
    provider_st = provider_stories()
    if bool(args.get(names.ACTIVE)) is False:
        args[names.ACTIVE] = ''
    else:
        args[names.ACTIVE] = 'and active is True'
    answer = provider.get_notifications(args)
    if args.get(names.ID_USER) and int(args.get(names.ID_USER)) in get_admins_ids(args):
        args['left_string'] = 'left'
    for id in answer:
        args[names.ID_STORIES] = id.get(names.ID_STORIES)
        id[names.ID_STORIES] = id.get(names.ID_STORIES)
        result = provider_st.get_stories(args)
        if result:
            for field in req_fields:
                id[field] = result[0].get(field)
    return answer
