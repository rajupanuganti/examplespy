from time import sleep
from threading import*

class hello(Thread):
    def run(self):
        for i in range(4):
            print('hello')
            sleep(1)

class pulihoraraja(Thread):
    def run(self):
        for i in range(4):
            print('pulihora raja')
            sleep(1)

t1 = hello()
t2 = pulihoraraja()

t1.start()
sleep(0.2)
t2.start()  

t1.join()
t2.join()

print('byeee')