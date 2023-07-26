#2wpp to swap two variables using given methods
""" 1)nav approach
2)using comma opertor
3)using arithmetic operations"""
p=int(input("enter first integer number :"))
q=int(input("enter second integer number :"))

#nav approach
#nav method use temp variable to swap numbers
"""temp=1-p
p=q
q=abs(temp-1)
print("first is :",p,"\nsecond is :",q)

#comma operator efficient than all
p,q=q,p

"""
"""
#using xor method
p=p^q
q=p^q
p=p^q
print("first is :",p,"\nsecond is :",q)
"""
#using arithmetic operation
p = p + q  
q = p - q 
p = p - q
print("first is :",p,"\nsecond is :",q)

