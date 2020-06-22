num = int(input('Enter a number : '))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,'is Not prime numner')
            break
    else:
        print(num,'is a Prime number')

       

else:
    print('enter grtr 1')
