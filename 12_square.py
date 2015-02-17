def square(n):
    '''eliminate the senario where users input string'''
    if type(n) is not int and type(n) is not float:
        raise RuntimeError, 'please pass in numeric values'
    return n*n
