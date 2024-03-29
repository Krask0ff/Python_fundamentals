import math

group_size = int(input())
days = int(input())
companions_count = 0
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 1 == 0:
        coins += 50
        coins -= 2 * group_size
    if day % 3 == 0:
        if day % 15 == 0:
            coins -= 5 * group_size
        else:
            coins -= 3 * group_size
    if day % 5 == 0:
        coins += 20 * group_size



print(f"{group_size} companions received {math.floor(coins / group_size)} coins each.")
