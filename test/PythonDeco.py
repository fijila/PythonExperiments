#!/bin/python3

import sys
import os
import datetime as dt
import inspect


# Add log function and inner function implementation here

def log(function):
    def printlog(*args, **kwdargs):
        str_template = "Accessed the function -'{}' with arguments {} {}".format(function.__name__,args,kwdargs)
        print(str_template )
        return function(str_template)

    return printlog


def greet(msg):
    return  msg


greet = log(greet)

'''Check the Tail section for input/output'''

if __name__ == "__main__":
       print( greet('hello world!'))
from functools import wraps

def decorator_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def square(x):
    return x**2

print(square.__name__)
def decorator_func(func):
    def wrapper(*args, **kwdargs):
        return func(*args, **kwdargs)
    wrapper.__name__ = func.__name__
    return wrapper


@decorator_func
def square(x):
    return x**2

print(square.__name__)