from app.route.profile.provider import Provider


def get_profile(args):
    provider = Provider()
    answer = provider.get_profile(args)
    return answer


def insert_profile(args):
    provider = Provider()
    answer = provider.insert_profile(args)
    return answer


def update_profile(args):
    provider = Provider()
    answer = provider.update_profile(args)
    return answer
