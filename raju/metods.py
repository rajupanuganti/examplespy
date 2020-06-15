class nike:
    company = 'US & co '

    def __init__(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def mul(self):
        return (self.n1*self.n2*self.n3)


s1 = nike(32,31,35)
print(s1.mul())
