class Point:
    def __init__(self, x1, y1, z1):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

    def __add__(self, other):
        x = self.x1 + other.x1
        y = self.y1 + other.y1
        z = self.z1 + other.z1
        p3 = Point(x, y, z)
        return p3

    def __str__(self):
        return  str(self.x1)+","+str(self.y1) + "," + str(self.z1)


p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
print(p1+p2)
print(p1)

