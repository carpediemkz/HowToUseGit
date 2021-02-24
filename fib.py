def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while 0 < n:
        result.append(b)
        a, b, n = b, a + b, n - 1
    return result


def main():
    while True:
        n = int(input("输入一个整数："))
        print("前{0}个斐波那契数字是: {1}".format(n, fib2(n)))


if __name__ == "__main__":
    main()
