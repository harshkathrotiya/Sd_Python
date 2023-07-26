# 9-3 wpp to read lines from text file and fisplay those words which are less than four characters
def less_four():
    myfile=open("demo.txt","r")
    st=myfile.read()
    str=st.split()
    count=0
    for i in str:
        if len(i)<4:
            count+=1        
    print(count)
    print(str)
    myfile.close()
less_four()

