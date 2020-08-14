def fib(num):
    fib_list = []
    if num <= 0:
        return fib_list
    else:
        x, y = 0, 1
        for i in range(num):
            fib_list.append(y)
            x, y = y, x + y
    return fib_list