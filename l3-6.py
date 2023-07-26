#add new item to a list after a specified item.
l1=["hello","what","about","now","days"]
res=list(filter(None,l1))
print(len(res))
res.insert(1,"dear") #insert is use for add element index wise
print(res)
