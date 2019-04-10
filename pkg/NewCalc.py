class Calculator:
    def calc(self,pasedOperation):
     
     
     if pasedOperation.operationName=="add":
       return pasedOperation.val1+pasedOperation.val2
     elif pasedOperation.operationName=="sub":
       return pasedOperation.val1-pasedOperation.val2
    
class OperationDetails:
    value1=0
    value2=0
    operationname="str"
    def __init__(self,value1,value2,operationname):
     self.val1=value1
     self.val2=value2
     self.operationName=operationname
operation1=OperationDetails(10,5,"sub")
calculator1=Calculator()
w=calculator1.calc(operation1)
print(w)
