num=int(input('number'))

def fact_gen(num):
 fact=1
 for i in range(1,num):
    fact*=i
    yield fact
n=fact_gen(num)
print(n)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))





