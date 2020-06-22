list1 = [25,89,5,4,6,2,32]
large = list1[0]
small = list1[0]
for i in range(0,len(list1)):
    if list1[i]>large:
        large=list1[i]

    if list1[i]<small:
        small=list1[i]


print(large,small)