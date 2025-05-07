from multiprocessing import Process
from time import sleep

class MyProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name=name

    def run(self):
        print(f"process {self.name} starts...")
        sleep(3)
        print(f"process {self.name} ends...")

if __name__=="__main__":
    print("main process starts")
    MyProcess("First Proc").start()
    MyProcess("Second Proc").start()
    print("main process ends")