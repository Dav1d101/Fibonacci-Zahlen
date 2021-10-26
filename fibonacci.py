#!/usr/bin/python3

print('Wich number do you want to know?')
n = int(input())
ordinal_number = "th"

def fib(n):
    fib_1 = 0
    fib_2 = 1
    fib_next = 0
    i = 0
    if n == 1:
        fib_n = fib_1
    if n == 2:
        fib_n = fib_2
    if n > 2:
        while i != n-2:
            fib_next = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_next
            i += 1
        fib_n = fib_next
    return fib_n

if n == 1:
    ordinal_number = "st"
elif n == 2:
    ordinal_number = "nd"
elif n == 3:
    ordinal_umber = "rd"

print("The "+ str(n) + ordinal_number + " number in the fibonacci row is "+ str(fib(n)))
