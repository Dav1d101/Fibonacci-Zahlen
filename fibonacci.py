#!/usr/bin/python3

print('Wich number do you want to know?')
n = int(input())
ordinal_number = "th"

def fib(n):
    fib_1 = 0
    fib_2 = 1
    fib_next = 0
    i = 0
    if n == 0:
        fib_n = fib_1
    elif n == 1:
        fib_n = fib_2
    elif n > 1:
        while i != n-1:
            fib_next = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_next
            i += 1
        fib_n = fib_next
    else:
        return -1    #returns -1 if n is a negative number
    return fib_n

fib_number = fib(n)
if n == 0:
    ordinal_number = ""
elif n == 1:
    ordinal_number = "st"
elif n == 2:
    ordinal_number = "nd"
elif n == 3:
    ordinal_umber = "rd"
if fib_number >= 0:
    print("The "+ str(n) + ordinal_number + " number in the fibonacci row is "+ str(fib_number)+"!")
else:
    print("there is no negative number in the fibonacci row!")
