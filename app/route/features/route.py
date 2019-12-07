# coding=utf-8
from app.api.base import base_name as names
from app.route.features.processor import *
from app.api.base.base_router import BaseRouter


class Features(BaseRouter):

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_feature_user(args)
        return answer, 200, names.HEADER


class FeaturesAdd(BaseRouter):
    def __init__(self):
        super().__init__()
        self.args = [names.NAME]

    def post(self):
        self._read_args()
        answer = insert_feature(self.data)
        return answer, 200, names.HEADER
