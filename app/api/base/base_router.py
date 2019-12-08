# coding=utf-8
import json
from flask_restful import Resource, reqparse
from app.api.base import base_name as names


class BaseRouter(Resource):
    """
    Базовый роут
    """
    _args = []

    def __init__(self):
        # Список параметров, которые считываются из запроса
        self.args = None
        # Словарь, содержащий данные считанные из запроса
        self.data = dict()

        self._parser = reqparse.RequestParser()

    def _read_args(self):
        """
        Метод вычитывает аргументы, описанные в self.args из запроса
        :return:
        """
        for arg in self.args:
            self._parser.add_argument(arg)
        self.data = self._parser.parse_args()
        if reqparse.request.data:
            self.data[names.URL] = json.loads(reqparse.request.data).get(names.URL)
            self.data[names.DESCRIPTION] = json.loads(reqparse.request.data).get(names.DESCRIPTION)
            self.data[names.ID_PROFILE] = json.loads(reqparse.request.data).get(names.ID_PROFILE)

    def get(self):
        return "OK", 200, names.CORS_HEADERS

    def post(self):
        return "OK", 200, names.CORS_HEADERS

    def delete(self):
        return "OK", 200, names.CORS_HEADERS

    def put(self):
        return "OK", 200, names.CORS_HEADERS

    def options(self):
        return "OK", 200, names.CORS_HEADERS

