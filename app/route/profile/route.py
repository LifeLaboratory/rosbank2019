# coding=utf-8
from app.api.base import base_name as names
from app.route.profile.processor import *
from app.api.base.base_router import BaseRouter


class Profile(BaseRouter):
    """
    Роут для получения профиля пользователя
    """
    def __init__(self):
        super().__init__()
        self.args = [names.FIO, names.DESCRIPTION, names.PHOTO, names.STATUS, names.TITLE]

    def get(self):
        args = {}
        answer = get_profile(args)
        return answer, 200, names.CORS_HEADERS
