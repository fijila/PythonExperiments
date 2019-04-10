import inspect
import doctest
import re
import math#def add2num(x, y):
#    """Adds two given numbers and returns the sum.
#    >>> add2num(6, 7)
#    13
#    >>> add2num(-8.5, 7)
#    -1.5
#    """
#    return x + y
#
#def mul(x, y):
#    """Multiplies two given numbers and returns the product.
#    >>> mul(6, 7)
#    42
#    >>> mul(-8, 7)
#    -56
#    """
#    return x * y
def mul(x, y):
    """Multiplies two given numbers and returns the product.
    >>> mul(6, 7)
    42
    >>> mul(-8, 7)
    -56
    """
    return x * y

def isPalindrome(x):
    # Write your doctests below.
    """
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
    ...
    ValueError: x must be a positive integer
    >>> isPalindrome('hello')
    Traceback (most recent call last):
    ...
    TypeError: x must be an integer

    """
    # Write the functionality below
    reverse=0
    if type(x)!= int:
        raise TypeError('x must be an integer')
    if x<0:
        raise ValueError('x must be a positive integer')

    if (str(x) == str(x)[::-1]):
        return True
    else:
        return False;


class Circle:

    def __init__(self, radius):
        # Define the doctests for __init__ method below
        """
        >>> circle=Circle(2.5)
        >>> circle.radius
        2.5
        """
        self.radius = radius

    def area(self):
        # Define the doctests for area method below
        """
        >>> circle=Circle(2.5)
        >>> circle.area()
        19.63
        """
        # Define the area functionality below
        a =math.pi * self.radius ** 2
        a = float("{0:.2f}".format(a))
        return a

    def circumference(self):
        # Define the doctests for circumference method below
        """
        >>> circle=Circle(2.5)
        >>> circle.circumference()
        15.71
        """
        # Define the circumference functionality below
        a=2 * math.pi * self.radius
        a=float("{0:.2f}".format(a))
        return a


if __name__ == '__main__':
    doctest.testmod()

    c2 = Circle(2.5)
    doc1 = inspect.getdoc(c2.__init__)
    doc2 = inspect.getdoc(c2.area)
    doc3 = inspect.getdoc(c2.circumference)

    class_count = len(re.findall(r'Circle', doc1))
    func1_count = len(re.findall(r'c1.radius', doc1))
    func1_val = len(re.findall(r'2.5', doc1))

    print(str(class_count), str(func1_count), str(func1_val))

    class_count = len(re.findall(r'Circle', doc2))
    func1_count = len(re.findall(r'c1.area', doc2))
    func1_val = len(re.findall(r'19.63', doc2))

    print(str(class_count), str(func1_count), str(func1_val))

    class_count = len(re.findall(r'Circle', doc3))
    func1_count = len(re.findall(r'c1.circumference', doc3))
    func1_val = len(re.findall(r'15.71', doc3))

    print(str(class_count), str(func1_count), str(func1_val))

