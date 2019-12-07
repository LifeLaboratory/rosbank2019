import requests
from app.api.base.base_name import *
from random import randint, choice
from time import sleep
from json import dumps, loads


platform = ['android', 'web']


def create_post(d):
    requests.post('http://127.0.0.1:13451/api/statistic', json=d)


for i in range(1, 1000):
    d = {
        ID_USER: randint(1, 123456789) % 5,
        ID_ACTION: randint(1, 123456789) % 5,
        NAME_PLATFORM: choice(platform)
    }
    create_post(loads(dumps(d)))
    # sleep(0.5)