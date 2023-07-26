# 9 wpp to reverse  order of words
s=input("enter the string :")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i+=1
   
for i in range(len(l1)):
    print(str(l1[i]))

"""
#output=l1
output=l1[0]+" "+l1[1]
print(output)
"""

