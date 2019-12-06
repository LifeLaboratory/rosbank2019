from app.route.statistic.provider import Provider


def statistic(statistic_data):
    provider = Provider()
    answer = provider.statistic(statistic_data)
    if isinstance(answer, list):
        answer = answer[0]
    return answer
