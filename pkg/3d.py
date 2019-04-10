class Point:
   def __init__ (self,x,y,z):
       self.x=x
       self.y=y
       self.z=z
   def __str__(self,x,y,z):
       self.x=x
       self.y=y
       self.z=z
p1=Point(4,2,9)
p2=Point('x','y','z')
print(p1.x,p1.y,p1.z)
print(p2.x,p2.y,p2.z)