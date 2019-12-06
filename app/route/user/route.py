# coding=utf-8
from app.api.base import base_name as names
from app.route.user.processor import *
from app.api.base.base_router import BaseRouter


class Auth(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.LOGIN, names.PASSWORD]

    def post(self):
        self._read_args()
        answer = auth(self.data)
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }


class Register(BaseRouter):
    def __init__(self):
        super().__init__()
        self.args = [names.LOGIN, names.PASSWORD, names.FIO, names.DESCRIPTION, names.PHOTO]

    def post(self):
        self._read_args()
        if ' ' in self.data.get(names.LOGIN) \
            or ' ' in self.data.get(names.PASSWORD) \
            or '' == self.data.get(names.FIO) \
            or '' == self.data.get(names.PHOTO) \
            or '' == self.data.get(names.DESCRIPTION):
            return {}
        answer = register(self.data)
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }
