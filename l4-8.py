#8as tuple is immutable wpp to show how change the tuple
#\and9 append a new item inyo tuple
t1=("antypathy",2,3.344,False)
t2=list(t1)
t2[1]="how"
t2.append("are")
t3=tuple(t2)
print(t3)