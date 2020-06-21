x = int(input('first num '))
y = int(input('second num '))

print('before swap is ',x,y)

x= x+y
y= x-y
x= x-y

print('after swap is ',x,y)