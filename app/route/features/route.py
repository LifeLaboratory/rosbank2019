# coding=utf-8
from app.api.base import base_name as names
from app.route.features.processor import *
from app.api.base.base_router import BaseRouter


class Features(BaseRouter):
    """
    Роут для получения испльзуемого функционала по ид пользователя
    """
    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_feature_user(args)
        return answer, 200, names.CORS_HEADERS


class FeaturesAdd(BaseRouter):
    """
    Роут для добавления функционала
    """
    def __init__(self):
        super().__init__()
        self.args = [names.NAME, names.ID_STORIES, names.URL, names.STATUS]

    def post(self):
        self._read_args()
        answer = insert_feature(self.data)
        return answer, 200, names.CORS_HEADERS
