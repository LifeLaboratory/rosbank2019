# coding=utf-8
from app.api.base import base_name as names
from app.route.stories.processor import *
from app.api.base.base_router import BaseRouter


class StoriesProfile(BaseRouter):
    """
    Роут работы со сторис
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.URL, 'type']

    def get(self, id_profile):
        self._read_args()
        self.data[names.ID_PROFILE] = id_profile
        answer = stories_profile(self.data)
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                                   'Access-Control-Allow-Methods': '*',
                                   'Access-Control-Allow-Headers': '*',
                                   }


class Stories(BaseRouter):
    """
    Роут работы со сторис
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.URL, names.ID_PROFILE, 'type']

    def post(self):
        self._read_args()
        answer = publicate_storie(self.data)
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }

    def get(self):
        self._read_args()
        answer = get_all_stories(self.data)
        return answer, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }


class StoriesStatus(BaseRouter):
    """
    Роут работы со сторис
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.STATUS, names.IS_LIKE, names.ID_NOTIFICATION]

    def post(self):
        self._read_args()
        answer = change_status(self.data)
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }


class StoriesInsert(BaseRouter):
    """
    Роут работы со сторис
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.URL]

    def post(self):
        self._read_args()
        answer = insert_stories(self.data)
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }


class StoriesUpdate(BaseRouter):
    """
    Роут работы со сторис
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.URL, names.ID_STORIES]

    def post(self):
        self._read_args()
        answer = update_stories(self.data)
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }


class StoriesList(BaseRouter):
    """
    Роут работы со сторис
    """

    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.URL, 'type']

    def get(self, id_user):
        self._read_args()
        self.data[names.ID_USER] = id_user
        answer = get_stories_list(self.data)
        return answer, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }
