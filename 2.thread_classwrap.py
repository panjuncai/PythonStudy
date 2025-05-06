from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name
    
    def run(self):
        for i in range(3):
            print(f"{self.name}:{i}")
            sleep(1)

if __name__=="__main__":
    print("main thread start")
    t1=MyThread("thread1")
    t2=MyThread("thread2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main thread end")
    