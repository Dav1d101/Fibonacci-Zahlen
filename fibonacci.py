#!/usr/bin/python3

print('Wich number do you want to know?')
n = int(input())
ordinal_number = "th"

def fib(n, fib_1, fib_2):
    fib_n = 0
    if n == 0 and fib_1 == 0:
        fib_n = fib_1
        return fib_1
    elif n == 1 and fib_2 == 1:
        fib_n = fib_2
        return fib_2
    elif n < 0:
        return -1
    fib_n = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = fib_n
    if n-2 != 0:
        n -= 1
        return fib(n, fib_1, fib_2)
    else:
        return fib_n
    

fib_number = fib(n ,0 ,1)
if n == 0:
    ordinal_number = ""
elif n == 1:
    ordinal_number = "st"
elif n == 2:
    ordinal_number = "nd"
elif n == 3:
    ordinal_number = "rd"
if fib_number >= 0:
    print("The "+ str(n) + ordinal_number + " number in the fibonacci row is "+ str(fib_number)+"!")
else:
    print("there is no negative number in the fibonacci row!")
