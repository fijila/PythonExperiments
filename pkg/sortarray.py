temp=0
list=[1,20,100,50,30,80]
listleng=len(list)
for i in range(0,listleng-1):
 for x in range(0,listleng-1):
    if(list[x]>list[x+1]):
     temp=list[x]
     list[x]=list[x+1]
     list[x+1]=temp
print(list)

