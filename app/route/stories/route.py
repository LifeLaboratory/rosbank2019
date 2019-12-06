# coding=utf-8
from app.api.base import base_name as names
from app.route.stories.processor import *
from app.api.base.base_router import BaseRouter


class Stories(BaseRouter):
    """
    Роут работы со сторис
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.URL, names.ID_PROFILE]

    def post(self):
        self._read_args()
        answer = publicate_storie(self.data)
        return answer or {}