num = int(input('Enter a number : '))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**4
    temp=temp//10

if num==sum:
    print('armstrong nummmm')

else:
    print('not armstrong nummm ')









