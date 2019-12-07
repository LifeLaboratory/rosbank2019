from app.route.features.provider import Provider
from app.route.notifications.provider import Provider as ProviderNot
from app.api.helper import get_admins
from app.api.base import base_name as names


def get_feature_user(data):
    provider = Provider()
    answer = provider.get_feature_user(data)
    return answer


def insert_feature(data):
    provider = Provider()
    provider_not = ProviderNot()
    answer = provider.insert_feature(data)
    data['url'] = ''
    data['status'] = ''
    data['id_stories'] = None
    answer = provider_not.insert_notification(data)[0]
    data[names.ID_NOTIFICATION] = answer.get(names.ID_NOTIFICATION)
    admin_ids = get_admins(data)
    for admin_id in admin_ids:
        data[names.ID_USER] = admin_id.get(names.ID_USER)
        provider_not.insert_notifications_users(data)
    return answer
