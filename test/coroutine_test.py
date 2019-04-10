#!/bin/python3

import sys


# Define 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwargs):
        c = coroutine_func(*args, **kwargs)
        next(c)
        return c

    return wrapper


# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        result = a * (x ** 2) + b
        print('Expression, ' + str(a) + '*x^2 + ' + str(b) + ', with x being ' + str(x) + ' equals ' + str(result))


# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    while True:
        x = yield;
        equation1 = linear_equation(3, 4)
        equation1.send(x)
        equation2 = linear_equation(2, -1)
        equation2.send(x)
    # code to send the input number to both the linear equations


def main(x):
    n = numberParser()
    #next(n)
    n.send(x)



if __name__ == "__main__":
    x = float(input())

    res = main(x);


