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
        return answer, 200, {'Access-Control-Allow-Origin': '*',
                             'Access-Control-Allow-Methods': '*',
                             'Access-Control-Allow-Headers': '*',
                             }
