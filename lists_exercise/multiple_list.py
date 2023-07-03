num_one = int(input())
num_two = int(input())
list = []
for i in range(num_one, num_one * num_two + 1, num_one):
    list.append(i)
print(list)