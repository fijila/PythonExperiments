class Printer:
    def __init__(self,maufacturer):
     self.maufacturer=maufacturer
    def print(self,person):
     print ("%s 's address is %s " % (person.name, person.address))
     print(person.name)
     print(person.address)
     print("Printed From %s printer" % self.maufacturer)
        

class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
printobj=Printer("Hp")
printobj1=Printer("Toshiba")

personobj=Person("fijila","uk")
printobj.print(personobj)
personobj1=Person("Fazeem","Bradford")
printobj.print(personobj1)
personobj2=Person("Faizan","Bradford")
printobj1.print(personobj2)

