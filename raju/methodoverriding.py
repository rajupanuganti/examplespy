class parent:
    def car(self):
        print('polo')

class child(parent):
    def __init__(self):
        print('verna')


o = child()