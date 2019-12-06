# coding=utf-8
import json
from flask_restful import Resource, reqparse
from app.api.base import base_name as names


class BaseRouter(Resource):
    _args = []

    def __init__(self):
        # Список параметров, которые считываются из запроса
        self.args = None
        # Словарь, содержащий данные считанные из запроса
        self.data = dict()

        self._parser = reqparse.RequestParser()

    def _read_args(self):
        for arg in self.args:
            self._parser.add_argument(arg)
        self.data = self._parser.parse_args()
        if reqparse.request.data:
            self.data[names.movement] = json.loads(reqparse.request.data.decode()).get(names.movement)

    def get(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def delete(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def put(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def options(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

