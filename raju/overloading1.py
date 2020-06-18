class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a,b):
        s = a+b
        return s

s1=student(12,13)

print(s1.sum(11,22))
