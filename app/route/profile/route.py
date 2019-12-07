# coding=utf-8
from app.api.base import base_name as names
from app.route.profile.processor import *
from app.api.base.base_router import BaseRouter


class Profile(BaseRouter):
    """
    Метод для получения профилей и обновления данных
    """
    def __init__(self):
        super().__init__()
        self.args = [names.FIO, names.DESCRIPTION, names.PHOTO, names.STATUS, names.TITLE]

    def get(self):
        args = {}
        answer = get_profile(args)
        return answer or {}, names.HEADER

    def post(self):
        args = {}
        answer = insert_profile(args)
        return answer or {}, names.HEADER

    def put(self, id_user):
        self._read_args()
        if id_user:
            self.data.update({names.ID_USER: id_user})
        answer = update_profile(self.data)
        return answer or {}, 200, names.HEADER
