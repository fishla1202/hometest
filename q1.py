def fib(n):
    f = dict()
    f[0] = 1
    f[1] = 1
    f[2] = 2

    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2] + f[i - 3]

    return f[n]


if __name__ == '__main__':
    print(fib(5))
