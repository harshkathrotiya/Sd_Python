# 9-4 wpp to count words in a text file those are ending with alphabet e.
def end_withe():
    myfile=open("demo.txt","r")
    st=myfile.read()
    str=st.split()
    count=0
    for i in str:
        if i[-1]=='e'or i[-1]=='E':
            count+=1        
    print(count)
    myfile.close()

end_withe()
