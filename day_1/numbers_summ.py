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

num_func([1,2,3,4,5,5,6])
