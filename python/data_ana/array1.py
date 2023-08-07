import array as arr
#creating an array with integer type
a=arr.array('i',[1,2,3])
#printing original array
print("klen is ",len(a))
b=1
print(b in a)
print("the new created array is  before insertion: ",end= " ")
for i in range(0,3):
    print(a[i],end=" ")
a.insert(1 ,3)             #1is index 4 is value
print("poped element is", a.pop(2))
# print(a.pop(2))#pop removes element from array
print("after insertion")
for i in range(0,3):
    print(a[i],end=" ")    
#creating an array with double typ
b=arr.array('d',[3.3456,343.35,456.45,456.0504,456.45])
#printing original array
b.remove(456.45)#it removes duplicatesS
print("\n th new created array is before append:",end=" ")
for i in range(0,4):
    print(b[i],end=" ")
print("after append")
b.append(3.45)
for i in range(0,4):
    print(b[i],end= " ")
    

