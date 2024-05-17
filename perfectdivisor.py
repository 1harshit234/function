def num(x):
    sum = 0
    for i in range(1,x+1):
        if ( x % i == 0):
            sum = sum + i
            return sum
    return sum == x
print(num((6)))
    