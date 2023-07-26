# l7-11 wpp that invokes a function after a specified period of time.

from time import sleep
def delay(fn,ms):
    sleep(ms/100)
    return fn

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

print(delay(add(10,20),100))
print(delay(sub(40,20),1000))
