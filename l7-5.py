# wpf that takes a number as a parameter and check whether the number is prime or not

def Is_prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else :
        for i in range(2,num):
            if num%2==0:
                 return True
        return False
n=int(input("enter number :"))
print(Is_prime(n))
