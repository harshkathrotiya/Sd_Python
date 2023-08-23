def facto(a):
    if a == 0 or a ==1 :
        return 1
    else:
        return (a * facto(a-1))
    
def primenum(num):
    if num==1:
       return "number is not prime"
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                return num,"is notprime"
                break
        else:
            return num,"isprime"
    else:
        return f'{num},"isnot prime"'