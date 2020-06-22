nterms = int(input('how many term u want: '))
a=0
b=1
count=2
if nterms<=0:
    print('positive enter chey ra babu...')

elif nterms==1:
    print(a)

else:
    print(a,',',b,end=',')
    while nterms>count:
        c=a+b
        print(c,end=',')
        a=b
        b=c
        count+=1