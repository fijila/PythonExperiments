try:
    a='elaephantrunning'
    b=len(a)
    print(b)
    if b>=10:
        raise ValueError('value is more than 10')
except TypeError as e:
    print(e)