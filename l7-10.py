# l7-10 wpp to access a function insight of a function.
def test(a):
    def add(b):
        nonlocal a #nonlocal means it access outside of block(function)
        a+=1
        return a+b
    return add
func=test(7)
print(func(4))



