class calculator:
    def add(self,a,b):
        sum=a+b
        return sum
    def substract(self,a,b):
        minus=a-b
        return minus
    def multply(self,a,b):
        mul=a*b
        return mul
    def division(self,a,b):
        div=a/b
        return div
calc=calculator()
print(calc.add(100,50))
print(calc.substract(100,50))
print(calc.multply(100,50))
print(calc.division(50,100))
class Printer:
    def __init__(self,maufacturer):
     self.maufacturer=maufacturer
    def print(self,person):
        
        print(person.name)
        print(person.address)
        print(self.maufacturer)
        

class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
printobj=Printer("Hp")
personobj=Person("fijila","uk")
printobj.print(personobj)
