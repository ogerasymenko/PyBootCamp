def func_info(func):
    """Decorator for printing info about passed function"""
    def func_name(*args):
        for a in args:
            print 'Arg type:', type(a)
            print 'Arg value:', a
        rs = func(*args)
        return rs
    return func_name
