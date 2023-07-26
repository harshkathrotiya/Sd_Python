#1 concantenate 2 list and string index wise
list1=["s","r","a","dh"]
list2=["a","d","r","am"]
"""l3=list1+list2
print(l3)
"""
l3=[i+j for i,j in zip(list1,list2)]
print(l3)