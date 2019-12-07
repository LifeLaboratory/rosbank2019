# coding=utf-8
from app.api.base import base_name as names
from app.route.statistic.processor import *
from app.api.base.base_router import BaseRouter


class Statistic(BaseRouter):
    """
    Роут для работы со статистикой
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.ID_ACTION, names.NAME_PLATFORM]

    def post(self):
        self._read_args()
        answer = statistic(self.data)
        return answer, 200, names.CORS_HEADERS

    def get(self):
        answer = get_statistic_list()
        return answer, 200, names.CORS_HEADERS


class StatisticView(BaseRouter):
    """
    Роут для получения статистики по ид пользователя
    """
    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_statistic(args)
        return answer, 200, names.CORS_HEADERS
