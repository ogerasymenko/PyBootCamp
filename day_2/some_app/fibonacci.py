import argparse
import sys


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
    parser = argparse.ArgumentParser(description='Number for processing.')
    parser.add_argument('-n', '--number', type=int, help='Integer nubmer for Fibonacci siquence')
    args = parser.parse_args()
    
    if not args.number:
        print('Args required. Type -h too see detail.')
        sys.exit(0)
    else:
        print(fibonacci(args.number))
