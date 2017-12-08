import argparse
import os

parser = argparse.ArgumentParser(description='Number for processing.')
parser.add_argument('-a', '--app', type=str, required=True, help='App to run: fibonacci or numbers')
parser.add_argument('-n', '--number', type=str, required=False, help='Integer nubmer for Fibonacci siquence')
args = parser.parse_args()

if args.app == 'numbers':
    os.system('python2 ./some_app/numbers_summ.py')
elif args.app == 'fibonacci':
    os.system('python2 ./some_app/fibonacci.py -n ' + args.number)
else:
    print 'wrong arguments'
