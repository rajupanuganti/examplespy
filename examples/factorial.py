x = int(input('Enter number '))
factorial = 1
if x<0:
    print('dengeyyy ra ')

elif x==0:
    print('fact is 1')

else:
    for i in range(1,x+1):
        factorial = factorial*i
    print('factorial value of ',x,'is :  ',factorial)