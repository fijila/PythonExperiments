def revestring(w):
   rev=0
   while w>0:
       d=w%10
       rev=rev*10+d
       w=w//10
   print(rev)
revestring(605)





