# l7 -hw write a  menu based program to do the following:
"""
1)check string is palindrome or not
2)check num is palindrome or not
3)check num is perfect or not
4)reverse the order of words in a given string
"""
def Is_palindrom_str(st):
    newst=st[::-1]
    if newst==st:
        return True
    else:
        return False
def Is_palin_num(num):
    num1=int(str(num)[::-1])
    if num==num1:
        return True
    else:
        return False
def Perfect_num(numb):
    tmp=0
    for i in range(1,numb):
        if(i%2==0):
            tmp+=i
    return tmp
def Orderof_word(x) :
   
    l=x.split()
    l1=[]
    i=0
    while i<len(l):
        l1.append(l[i][::-1])
        i+=1
   
    #for i in range(len(l1)):
     #   print(l1[i])
    return l1
    
print("menu")    
print("1) check stringis palindrome or not")
print("2)check num is palindrome or not")
print("3}check num is  perfect or not")
print("4)reverse the order of words in a given string")
choice=int(input("plz enter your choice  :"))
if choice==1 or choice==4:
    str=input("plz enter the string :")
    if choice==1:
        a=Is_palindrom_str(str)
        if a:
            print("string is palindrome")
        else :
            print("string is not palindrome")
    if choice==4:
        b=Orderof_word(str)
        print(b)

if choice==2 or choice==3:
    
    number=int(input("enter the num :"))
    if choice==2:
        c=Is_palin_num(number)
        if c:
            print("num is palindrome")
        else :
            print("num is not palindrome")

    if choice==3:
        d=Perfect_num(number)
        if d==number:
            print("number is perfet")
        else :
            print("number is not perfect")


