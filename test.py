def func(n):
    while n >= 0:
        yield n
        n -= 1

for i in func(10):
    print(i)