# 19.1 (pg 265)
def swap_in_place(a,b):
    ''' Takes two integer values and swaps them in place. '''
    a = (a+b)
    b = (a-b)
    a = (a-b)
    return a,b

