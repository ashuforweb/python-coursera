'''Fibonacci series in python 3'''
m = input('Please Enter Integer:')
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b
    print()
fib(int(m))
