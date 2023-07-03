number_of_lines = int(input())
sum = 0
sum2 = 0
for number in range(number_of_lines):
    char = input()
    sum += ord(char)
    sum2 += sum
    sum = 0
print(f"The sum equals: {sum2}")