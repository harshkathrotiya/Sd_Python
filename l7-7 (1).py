# l7-7 wpp to check whether a string is pangram
import string

def pangram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset<=set(str1.lower())
str1="the quick brown fox jump over the lazy DOgs"
print(pangram(str1))
