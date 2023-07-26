# 9-6 a binary file has structure book num,book name,author,price
"""
1)write a use define funct.. to inp data for a record and add in binary file.
2)write a function which accept the author name as parameter and count and return num of books by 
  the given author are stored in binary file.
"""

import pickle
def createfile():
    fp=open("book.dat","ab")
    book_no=int(input("enter book no :"))
    book_name=input("enter book name :")
    author=input("enter author name :")
    price=float(input("enter the price :"))
    record=[book_no,book_name,author,price]
    pickle.dump(record,fp)
    fp.close()
def countrecord(author):
    fc=open("book.dat","rb")
    count=0
    try:
         while True:
            record=pickle.load(fc)
            print(record)
            if record[2]==author:
                count=count+1
    except EOFError:
        pass
    return count
    fc.close()


def count_books(bname):
    fp=open("book.dat","rb")
    count=0
    try:
        while True:
            record=pickle.load(fp)
            if record[1]==bname:
                count+=1
    except EOFError:
        pass
    return count
    fp.close()


def test():
    while True:
        createfile()
        ch=input("you should check again ?(y/n) :")
        if ch in 'Nn':
            break
    author=input("enter author name :")
    book=input("enter the bookname to find count :")
    n=countrecord(author)
    bookcount=count_books(book)
    print("no of books of author is : ",n)
    print("count of books you finded is :",bookcount)
test()


