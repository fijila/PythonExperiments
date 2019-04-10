k=input('what number?')
n=int(k)
def fib_gen(n):
 s=0
 a=0
 b=1
 i=0
 print(0)
 print(1)
 for i in range(n):
    s = a + b
    yield s
    a=b
    b=s
fs=fib_gen(n)
print(fs)
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))