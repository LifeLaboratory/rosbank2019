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
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }


class StoriesView(BaseRouter):
    """
    Роут работы со сторис
    """
    def __init__(self):
        super().__init__()
        self.args = [names.ID_STORIES, names.ID_USER, names.STATUS, names.IS_LIKE]

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
        self.args = [names.ID_STORIES, names.ID_USER, names.STATUS, names.IS_LIKE]

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_storis_list(args)
        return answer
