def fib(n):
    f = dict()
    f[1] = 2
    f[2] = 2

    if n == 1:
        return 1
    elif n == 2:
        return 2

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


if __name__ == '__main__':
    print(fib(5))
