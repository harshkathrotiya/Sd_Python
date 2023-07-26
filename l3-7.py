#wpp to extend nest4ed list by adding the sublist
l1=["a","b","c",["d","e",["f","g","h"]]]
sub_list=["h","i","j"]
l1[3][2].extend(sub_list)
print(l1[3])
print(l1[3][2])
print(l1[3][2][0])
#extend adds new elements into list,size of list is increase.
