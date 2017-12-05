def fibonacci(n):
    """Function accept number and return string with Fibonacci siquence for this number"""
    numbers = []
    a = 0
    b = 1
    for i in range(n):
        numbers.append(str(a))
        a, b = b, a+b
    return ', '.join(numbers)


if __name__ == '__main__':
    print(fibonacci(7))
