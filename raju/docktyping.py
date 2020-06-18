class VScode:
    def excute(self):
        print('compiling')
        print('running')

class mycomp:
    def excute(self):
        print('filter')
        print('beauty')
        print('runnn,compiling')

class Laptop():
    def code(self,ide):
        ide.excute()

ide = VScode()
lap1 = Laptop()
lap1.code(ide)