class A:

    def __init__(self, val):
        self.x = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @x.deleter
    def x(self):
        del self.__x


a = A(7)
del a.x
print(a.x)


class A:

    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

a = A(7)
a.x = 10
print(a.x)

