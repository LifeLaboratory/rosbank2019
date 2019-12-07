from app.route.features.provider import Provider


def get_feature_user(data):
    provider = Provider()
    answer = provider.get_feature_user(data)
    return answer


def insert_feature(data):
    provider = Provider()
    answer = provider.insert_feature(data)
    return answer
