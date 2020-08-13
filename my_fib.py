#一、编程题目
#########################
#    1
#########################
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 请编写一个函数输入n, 输出n个斐波那契数列的列表。 如：fib(5) -> [1, 1, 2, 3, 5]

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

#fib(5) -> [1, 1, 2, 3, 5]


