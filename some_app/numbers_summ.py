import argparse
from func_info import func_info


@func_info
def num_func(arg):
    """Function accept string with integers separeted by comma,
    and returns type list"""
    num_list = []
    arr = []
    
    if type(arg) == list:
        num_list = arg
    elif type(arg) == tuple:
        num_list = list(arg)
    elif type(arg) == str:
        num_list = [int(x.strip()) for x in arg.split(',')]
    else:
        raise TypeError('Wrong input data type')
    
    for index, element in enumerate(num_list):
        for next_element in num_list[index+1:]:
            if (element+next_element == 10) and \
            ((arr.count((element, next_element)) < 1) and 
             (arr.count((next_element, element)) < 1)):
                arr.append((element, next_element))
            else:
                continue

    return arr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Numbers via comma for processing.')
    parser.add_argument('-n', '--numbers', type=str, required=True, help='Numbres like 1,2,3')
    args = parser.parse_args()
    result = num_func(args.numbers)
    if result:
        for r in result:
            print r[0], '+', r[1]
