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


def insert_stories(args):
    provider = Provider()
    answer = provider.insert_stories(args)[0]
    args['id_stories'] = answer.get('id_stories')
    args['position'] = 0
    for image in args.get('url'):
        args['url'] = image
        provider.insert_image(args)
    return 'OK'


def change_status(args):
    provider = Provider()
    status = provider.select_status(args)
    args['is_open'] = args['status'] == 'open'
    args['is_view'] = args['status'] == 'view'
    if status:
        answer = provider.update_status(args)
    else:
        answer = provider.insert_status(args)
    return 'OK'
