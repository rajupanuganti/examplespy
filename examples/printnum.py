n = int(input('Enter a num of row :'))
for row in range(n):
    for col in range(1,n-row+1):
        print(col,end='')

    print()
