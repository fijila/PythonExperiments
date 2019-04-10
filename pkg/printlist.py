class Printer:
    def __init__(self,maufacturer):
     self.maufacturer=maufacturer
    def print(self,personlist):
        for i in personlist:
            print(i.name,i.address)
        print("printed from %s printer" % self.maufacturer)
        
        

class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
printobj=Printer("Hp")
printobj1=Printer("Toshiba")
personlist=[]
personobj=Person("fijila","uk")
personlist.append(personobj)
5
personobj1=Person("Fazeem","leeds")
personlist.append(personobj1)

personobj2=Person("Faizan","Bradford")
personlist.append(personobj2)
printobj1.print(personlist)

