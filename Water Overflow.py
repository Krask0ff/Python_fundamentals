number_of_lines = int(input())
water_tank_capacity = 255
tank_loaded = 0

for i in range(number_of_lines):
    liters_of_water = int(input())
    if water_tank_capacity >= liters_of_water:
        water_tank_capacity -= liters_of_water
        tank_loaded += liters_of_water

    elif liters_of_water > water_tank_capacity:
        print("Insufficient capacity!")

print(tank_loaded)