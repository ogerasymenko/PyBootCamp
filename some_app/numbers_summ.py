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
def num_func(num_list):
    """Function accept list with integers, print unique pairs wich equal 10
    and returns None"""
    arr = []
    for i in num_list:
        for n in num_list[1:]:
            if (i+n == 10) and ((arr.count((i, n)) < 1) and (arr.count((n, i)) < 1)):
                arr.append((i, n))
            else:
                continue 
    return arr

if __name__ == '__main__':
    result = num_func((1,2,3,4,5,5,6))
    for r in result:
        print r[0], '+', r[1]
