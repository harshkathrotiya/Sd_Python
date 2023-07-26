# 8 wpp to display all positions of substring in a given main string

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

        