l1=[22,85,12,44,96,77,1]
temp = 0
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]<l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
for i in range(0,len(l1)):
    print(l1[i],end=' ')