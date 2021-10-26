#!/usr/bin/python3

n = int(input('wie viele Zahlen sollen angegeben werden?'))

def fib(n):
    fib_1 = 0
    fib_2 = 1
    fib_next = 0    
    if n == 1:
        fib_n = fib_1
    if n == 2:
        fib_n = fib_2
    if n > 2:
        for i in range(n-2):
            fib_next = fib_2+fib_1
            fib_1 = fib_2
            fib_2 = fib_next
        fib_n = fib_next
    return fib_n

print(fib(n))
