string = str(input())
number = 0
number2 = 0

while string != "End":

    for i in string:
        number = ord(i)
        number2 = ord(i)
        char = chr(number)
        char2 = chr(number2)
        print(char, end= '')
        print(char2, end= '')
    string = str(input())