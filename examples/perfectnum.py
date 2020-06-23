n= int(input('enter a num: '))
result=0
for i in range(1,n):
    if n%i==0:
        result=result+i
if result==n:
    print(n,'is perfect num')
else:
    print('not perfect num ')