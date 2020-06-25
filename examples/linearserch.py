def search(list,n):
    i = 0
    while i<len(list):
        if list[i] == n:
            return True
        i = i+1
    return False

list = [2,3,4,5,7,8]
n = int(input('enter a num:  '))
if search(list,n):
    print('found')
else:
    print('mingindi ')