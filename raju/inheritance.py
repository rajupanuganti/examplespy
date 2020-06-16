class A:
    def __init__(self):
        print('init A')

    def feat1(self):
        print('feat1')

class B:
    def __init__(self):
        super().__init__()
        print('init B')

    def feat2(self):
        print('feat2')

class c(A,B):
    def __init__(self):
        super().__init__()
        print('init C')


q1 = c()