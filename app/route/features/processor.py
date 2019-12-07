from app.route.features.provider import Provider


def get_feature_user(data):
    provider = Provider()
    answer = provider.get_feature_user(data)
    return answer
