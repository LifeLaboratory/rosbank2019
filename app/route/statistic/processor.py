from app.route.statistic.provider import Provider


def statistic(statistic_data):
    provider = Provider()
    answer = provider.statistic(statistic_data)
    return answer


def get_statistic(args):
    provider = Provider()
    answer = provider.get_statistic(args)
    return answer


def get_statistic_list():
    provider = Provider()
    answer = provider.get_statistic_list()
    return answer
