try:
    a=102
    if a>=100:
        raise ValueError('value is not between 102')
except TypeError as e:
    print(e)


