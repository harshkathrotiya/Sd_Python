#6 wpf to check perfect num

def perfect_no(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum

no=int(input('enter num :'))
result=perfect_no(no)
if result==no:
    print(no,"is perfect")
else :
    print(no,"is not perfect")