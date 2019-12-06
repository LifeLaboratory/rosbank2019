# coding=utf-8
from app.api.base import base_name as names
from app.route.notifications.processor import *
from app.api.base.base_router import BaseRouter


class Notification(BaseRouter):
    """
    Роут работы с уведомлениями
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_NOTIFICATION, names.NAME, names.URL, names.ID_PROFILE, names.STATUS]

    def post(self):
        self._read_args()
        answer = add_notification(self.data)
        return answer or {}

    def put(self, id_user):
        self._read_args()
        if id_user:
            self.data.update({names.ID_USER: id_user})
        answer = update_profile(self.data)
        return answer or {}


class Notification_get(BaseRouter):
    """
    Роут работы с уведомлениями
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_NOTIFICATION, names.NAME, names.URL, names.ID_PROFILE, names.STATUS]

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_notification(args)
        return answer or {}
