# 9-1 wpp to count and display the total number of words in a text file

def count_words():
    fp=open("demo.txt","r")
    count=0
    d=fp.read()
    words=d.split()
    #print("words :",words)
    for i in words:
        count+=1
    print("number of words are ",count)
    fp.close()


count_words()