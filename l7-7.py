# l7-7 wrpp to check whether a string is pangram or not.
import sys,string

def pangram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset<=(str1.lower())
str1="the quick brown fox jump over the lazy dogsu"
print(pangram(str1))

