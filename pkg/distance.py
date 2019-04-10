import math
class Point:
    def __init__(self, x1, y1, z1):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

def distance(p1,p2):
    distane = math.sqrt((p1.x1 -p2.x1) ** 2 + (p1.y1 - p2.y1) ** 2 + (p1.z1 - p2.z1) ** 2)
    return distane

p1 = Point(4,5,6)
p2 = Point(-2,-1,4)
print(distance(p1,p2))

