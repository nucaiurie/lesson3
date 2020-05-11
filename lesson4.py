import wikipedia
from emoji import emojize
import datetime
from functions import *

a = {'name': 'Oleg', 'health': 10}
b = {'name': 'Vologhea', 'health': 10}

print(f'{a.get("name")} attacks {b.get("name")} ')

b.update({"health": b.get("health")-attack()})
print(b)

print(f'{b.get("name")} attacks {a.get("name")} deals')
b.update({"health": a.get("health")-attack()})
print(b)

while True:
    print(f'{a.get("name")} wants to trick or run?')
    x = input()
    print(x)
    if x == 'trick':
        t = trick()
        live_or_die(t, a.get("name"))
        break
    else:
        r = run()
        live_or_die(r, a.get("name"))
    break
