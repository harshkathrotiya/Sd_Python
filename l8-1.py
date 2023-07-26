# l8-1 waf in python to print fibonacci series upto n terms

def fib(n):
    a=0
    b=1
    c=0
    print(a)
    print(b)
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
fib(12)   



