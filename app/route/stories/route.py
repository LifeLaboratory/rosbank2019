# coding=utf-8
from app.route.stories.processor import *
from app.api.base.base_router import BaseRouter
from app.api.base import base_name as names


class StoriesProfile(BaseRouter):
    """
    Роут работы для получения историй по ид пользователя
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.URL, names.TYPE]

    def get(self, id_profile):
        self._read_args()
        self.data[names.ID_PROFILE] = id_profile
        answer = stories_profile(self.data)
        return answer, 200, names.CORS_HEADERS


class Stories(BaseRouter):
    """
    Роут работы для добавления и получения всех историй
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.URL, names.ID_PROFILE, names.TYPE]

    def post(self):
        self._read_args()
        answer = publicate_storie(self.data)
        return answer, 200, names.CORS_HEADERS

    def get(self):
        self._read_args()
        answer = get_all_stories(self.data)
        return answer, 200, names.CORS_HEADERS


class StoriesStatus(BaseRouter):
    """
    Роут для обновления статуса историй
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.STATUS, names.IS_LIKE, names.ID_NOTIFICATION]

    def post(self):
        self._read_args()
        answer = change_status(self.data)
        return answer, 200, names.CORS_HEADERS


class StoriesInsert(BaseRouter):
    """
    Роут для добавления историй
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.URL, names.DESCRIPTION]

    def post(self):
        self._read_args()
        answer = insert_stories(self.data)
        return answer, 200, names.CORS_HEADERS


class StoriesUpdate(BaseRouter):
    """
    Роут для обновления историй
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.URL, names.ID_STORIES]

    def post(self):
        self._read_args()
        answer = update_stories(self.data)
        return answer, 200, names.CORS_HEADERS


class StoriesList(BaseRouter):
    """
    Роут для получниея всех историй для пользователя
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.URL, names.TYPE]

    def get(self, id_user):
        self._read_args()
        self.data[names.ID_USER] = id_user
        answer = get_stories_list(self.data)
        return answer, 200, names.CORS_HEADERS
