def no(number):
    y = 1
    for x in range(number, 1,-1):
     y = x*y
    print(y)
number = int(input("write the numner which you want"))
no(number)
#if u want to take the input from the user then you need to take it before the final output in the last lines