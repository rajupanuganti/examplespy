def reverse(s1):
    str = ''
    for i in s1:
        str=i+str
    return str
s1 = 'kanakachary'
print(reverse(s1))