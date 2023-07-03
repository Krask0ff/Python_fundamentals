import math
number_of_people = int(input())
capacity = int(input())
one_more_course = 1
full_courses = math.ceil(number_of_people / capacity)
print(full_courses)