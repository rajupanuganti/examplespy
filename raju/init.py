class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config',self.cpu,self.ram)

comp1 = computer('i8',32)
comp2 = computer('pathhi',90)

comp1.config()
comp2.config()