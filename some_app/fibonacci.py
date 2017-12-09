import argparse


def func_info(func):
    """Decorator for printing info about passed function"""
    def func_name(*args):
        for a in args:
            print type(a)
            print a
        rs = func(*args)
        return rs
    return func_name
                  

@func_info
def fibonacci(n):
    """Function accept number and return string with Fibonacci siquence for this number"""
    numbers = []
    a = 0
    b = 1
    for i in range(int(n)):
        numbers.append(str(a))
        a, b = b, a+b
    return ', '.join(numbers)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Number for processing.')
    parser.add_argument('-n', '--number', type=int, required=True, help='Integer nubmer for Fibonacci siquence')
    parser.add_argument('-u', '--use', action='store_true', help="A number to print")
    args = parser.parse_args()
    print(fibonacci(args.number))
