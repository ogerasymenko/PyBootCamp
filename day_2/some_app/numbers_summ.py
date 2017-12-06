def func_info(func):
    """Decorator for printing info about passed function"""
    def info(*args):
        for a in args:
            print('argumet: {}\narg type: {}\ndecorated func name: {}'.format(a, type(a), func.__name__))
        rs = func(*args)
        return rs
    return info


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
    for a in arr:
        print a[0], '+', a[1]
    
    return None

if __name__ == '__main__':
    num_func((1,2,3,4,5,5,6))
