import wikipedia
import emoji
from functions import attack

a = {'name': 'Oleg', 'health': 10}
b = {'name': 'Vologhea', 'health': 10}

print(f'{a.get("name")} attacks {b.get("name")} deals')

b.update({"health": b.get("health")-attack()})


print(b)

