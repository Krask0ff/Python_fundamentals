text = input().split()
list = []
for i in text:
    list.append(i)
new_list = [eval(i) for i in list]
opposite = [-i for i in new_list]
print(opposite)