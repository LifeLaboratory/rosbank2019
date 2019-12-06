from app.route.stories.provider import Provider
from app.api.base import base_name as names
from app.api.helper import get_id_user_by_profile


def publicate_storie(args):
    provider = Provider()
    id_users = get_id_user_by_profile(args)
    for id_user in id_users:
        args[names.ID_USER] = id_user.get(names.ID_USER)
        answer = provider.publicate_storie(args)
    return 'OK'
