
n = int(input('wie viele Zahlen sollen angegeben werden?'))

fib_1 = 0
fib_2 = 0
fib_next = 0    
if n >= 1:
	print(fib_1)
if n >= 2:
	print(fib_2)
if n > 2:
    for i in range(n-2):
        fib_next = fib_2+fib_1
        fib_1 = fib_2
        fib_2 = fib_next
        print(fib_next)
