fib = [0] * (20)

fib[0] = 0
fib[1] = 1
con = 1
for i in range(2, 19 + 1, 1):
    fib[i] = fib[i - 1] + fib[i - 2]
for i in range(0, 19 + 1, 1):
    print("O " + str(con) + " termo: " + str(fib[i]))
    con = con + 1
