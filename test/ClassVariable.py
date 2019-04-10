class Circle:
    no_of_circles = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.no_of_circles = Circle.no_of_circles + 1

    def area(self):
        return Circle.getPi() * self.radius ** 2

    @classmethod
    def getCircleCount(cls):
        return Circle.no_of_circles

    @staticmethod
    def getPi():
        return 3.14