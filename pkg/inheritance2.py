class Vehicle:
    def __init__(self,name,color):
     self.__name=name
     self.__color=color
    def getName(self):
      return self.__name
    def getColor(self):
        return self.__color
    def Result(self):
     return "My lorry "+self.getName()+" in "+self.getColor()
     
class Car(Vehicle):
    def __init__(self,name,color,model):
     super().__init__(name,color)
     self.__model=model
    def Result(self):
     return "My car "+self.getName()+" in "+self.getColor()+" is "+self.__model+" model. "
   
class Lorry(Vehicle):
    def __init__(self,name,color):
     super().__init__(name,color)
     
    

carobj=Car("vento","red","g5467")
w=carobj.Result()
print(w)
lorryobj=Lorry("benz","black")
y=lorryobj.Result()
print(y)
