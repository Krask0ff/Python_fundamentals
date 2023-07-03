budged = float(input())
price_for_1kg_flour = float(input())
price_for_1pack_of_eggs = price_for_1kg_flour * 0.75
price_for_1l_milk = price_for_1kg_flour * 1.25
price_for_250ml_of_milk = price_for_1l_milk / 4
total_price_for_one_bread = price_for_250ml_of_milk + price_for_1pack_of_eggs + price_for_1kg_flour
colored_eggs = 0
bread_count = 0
total_money_spent = 0

while budged > 0:
    budged = budged - total_price_for_one_bread
    total_money_spent += total_price_for_one_bread
    colored_eggs += 1
    bread_count += 1
    if bread_count == 3:
        colored_eggs -= 2
for every_third_bread in range(0, -1, 3):
    colored_eggs -= bread_count - 2
print(colored_eggs)
print(bread_count)