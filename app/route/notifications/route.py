# coding=utf-8
from app.api.base import base_name as names
from app.route.notifications.processor import *
from app.api.base.base_router import BaseRouter


class Notification(BaseRouter):
    """
    Роут для добавления уведомлений
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_NOTIFICATION, names.NAME, names.URL, names.ID_PROFILE, names.STATUS, names.ID_STORIES,
                     names.ID_STORIES]

    def post(self):
        self._read_args()
        answer = add_notification(self.data)
        return answer, 200, names.CORS_HEADERS


class NotificationGet(BaseRouter):
    """
    Роут получения уведомлений по ид пользователя
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_NOTIFICATION, names.NAME, names.URL, names.ID_PROFILE, names.STATUS, names.ACTIVE]

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_notification(args)
        return answer, 200, names.CORS_HEADERS
