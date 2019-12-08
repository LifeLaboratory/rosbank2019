from app.route.features.provider import Provider
from app.route.notifications.provider import Provider as ProviderNot
from app.api.helper import get_admins
from app.api.base import base_name as names


def get_feature_user(data):
    """
    Получить используемый функционал по ид пользователя
    :param data:
    :return:
    """
    provider = Provider()
    answer = provider.get_feature_user(data)
    return answer


def insert_feature(data):
    """
    Добавить новый функционал
    :param data:
    :return:
    """
    provider = Provider()
    provider_not = ProviderNot()
    provider.insert_feature(data)
    answer = provider_not.insert_notification(data)[0]
    data[names.ID_NOTIFICATION] = answer.get(names.ID_NOTIFICATION)
    admin_ids = get_admins(data)
    for admin_id in admin_ids:
        data[names.ID_USER] = admin_id.get(names.ID_USER)
        provider_not.insert_notifications_users(data)
    return answer
