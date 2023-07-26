# 7 # wpp to check string is palindrom or not

str1=input("enter the string :")
newstr=str1[::-1]
if str1==newstr:
    print("string is palindrome")
else:
    print("string is not palindrom")
    