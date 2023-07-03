quantity = int(input())
days = int(input())

ornament_set = 2
Tree_skirt = 5
Tree_garlands = 3
Tree_lights = 3
total_spent = 0
total_spirit = 0
for every_second_day in range(0, days , 2):
    total_spent += 2 * quantity
    total_spirit += 5
    # if day // 2 == 0:
    #     total_spent += 2 * quantity
    #     total_spirit += 5
    # if day // 3 == 0:
    #     total_spent += 5 + 3 * quantity
    #     total_spirit += 13
    # if day // 5 == 0:
    #     total_spent += 3 * quantity
    #     total_spirit += 17
    # if day // 15 == 0:
    #     total_spirit += 30
    # if day // 10 == 0:
    #     total_spirit -= 20
    #     total_spent += 5 + 3 + 3
# elif days // 11 == 0:
#
print(total_spirit)
print(total_spent)