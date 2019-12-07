from app.route.statistic.provider import Provider


def statistic(statistic_data):
    """
    Добавить статистику
    :param statistic_data:
    :return:
    """
    provider = Provider()
    answer = provider.statistic(statistic_data)
    return answer


def get_statistic(args):
    """
    Получить статистику по ид пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_statistic(args)
    return answer


def get_statistic_list():
    """
    Получить всю статистику по пользователям
    :return:
    """
    provider = Provider()
    answer = provider.get_statistic_list()
    return answer
