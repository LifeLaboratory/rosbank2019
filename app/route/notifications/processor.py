from app.route.notifications.provider import Provider
from app.api.base import base_name as names
from app.api.helper import get_id_user_by_profile


def add_notification(args):
    provider = Provider()
    answer = provider.insert_notification(args)[0]
    args[names.ID_NOTIFICATION] = answer.get(names.ID_NOTIFICATION)
    id_users = get_id_user_by_profile(args)
    for id_user in id_users:
        args[names.ID_USER] = id_user.get(names.ID_USER)
        provider.insert_notifications_users(args)
    return answer


def get_notification(args):
    provider = Provider()
    answer = provider.get_notifications(args)
    return answer


def update_profile(args):
    provider = Provider()
    answer = provider.update_profile(args)
    return answer
