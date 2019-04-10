#!/bin/python3

import sys
import os


# Add the factory function implementation here
def factory(n=0):

    def current():
        return n
    def counter():
        nonlocal n
        n+=1
        return n

    return current,counter

f_current,f_counter, = factory((2))
print(f_current())
print(f_counter())

#-------------------
#def factory(n=0):

    #def current():
        #return n


    #return current,counter

#f_current, f_counter = factory(int(input()))
#---------------------------------
if __name__ == "__main__":
        func_lst = [f_current, f_counter]
        res_lst = list()
        for func in func_lst:
            res_lst.append(func())




v = 'Hello'

def f():
    v = 'World'
    return v

print(f())
print(v)



def f(x):

  return 3*x

def g(x):
   return 4*x

print(f(g(2)))



def outer(x, y):

    def inner1():
        return x+y

    def inner2(z):
        return inner1() + z

    return inner2


f = outer(10, 25)

print(f(15))