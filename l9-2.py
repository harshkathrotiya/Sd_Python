# 9-2 wpp to read lines from a text file to  find and display the occurances of the word

def occurancesof_words():
    fp=open("demo.txt","r")
    str=fp.read()
    str.lower
    str.split()
    count=0
    for i in str:
        if i=="The" or i=="THe" or i=="the":
            count+=1
        else :
            print("no words word")
    print(count)
    fp.close()

occurancesof_words()