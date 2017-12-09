import argparse
from some_app import fibonacci
from some_app import num_func

parser = argparse.ArgumentParser(description='Number for processing.')
group = parser.add_argument_group("Parameters")
parser.add_argument('-a', '--app', type=str, required=True, help='App to run: fibonacci or numbers')
parser.add_argument('-n', '--number', type=str, required=True, action='store',
                    help='One number for fibonacci sequence or Sequence of numbers via comma for numbers')
args = parser.parse_args()

if args.app == 'numbers':
    result = num_func(args.number)
    if result:
        for r in result:
            print r[0], '+', r[1]
elif args.app == 'fibonacci':
    print(fibonacci(args.number))
else:
    print 'Wrong arguments'
