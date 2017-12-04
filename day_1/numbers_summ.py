def num_func(num_list):
    """Function accept list with numbers and returns
    list with unique pairs wich equal 10"""
    arr = []
    for i in num_list:
        for n in num_list[1:]:
            if (i+n == 10) and ((arr.count((i, n)) < 1) and (arr.count((n, i)) < 1)):
                arr.append((i, n))
            else:
                continue
    return arr

print(num_func([2,8,4,5,5,6,2,8,10,0]))
