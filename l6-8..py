# 1 wpp to display star in right angle triangle foam.

string =input("enter the string :")
sub= input("enter sub strihg :")
f= 0
k = 0
for i in range(0, len(string)):
    k = i
    f = 0
    for j in range(0, len(sub)):
        if string[k] != sub[j]:
            f = 1
        if f:
            break
        k = k + 1
    if f == 0:
       
        print(sub,"is at index",i)
 
st=input("plz enter the main string :");
substr =input("enter the substring for find :")
i = 0
while True:
    index = st.find(substr,i)
    if index == -1:
        break
    else:
        print(substr,"is at index",index)
        i = index + 1