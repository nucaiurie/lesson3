import random
import wikipedia
from emoji import emojize
import datetime


def attack():
    return random.randint(2, 5)


def heal():
    return random.randint(1, 6)


def run():
    a = random.randint(1, 10)
    if a < 5:
        return 'failed'
    else:
        return 'success'


def trick():
    a = random.randint(1, 2)
    if a < 2:
        return 'failed'
    else:
        return 'success'


def live_or_die(status, name):
    if status == 'failed':
        print(f'At this date, {datetime.datetime.today()}, {name},died')
        print(f'Here lies {wikipedia.summary(name, sentences=1)}')
    else:
        print(f'At this date, {datetime.datetime.today()}, {name},lived')
        print(f'The man who runs free is {wikipedia.summary(name, sentences=1)}')
        print(emojize(':thumbs_up:'))
