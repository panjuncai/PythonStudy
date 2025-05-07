# 需求：
# 实现两个进程间通信
# 进程1发起一条消息
# 进程2读取进程1的消息
# 反之亦然

# 思路，设计MyProcess类
# 传入目标读取的List和写入List
# 在主进程中，设置Process1的目标读取List即Process2的
# 在主进程中，设置Process2的目标读取List即Process1的
# 写入同理

from multiprocessing import Process,Queue
from threading import Thread
from time import sleep

class MyProcess(Process):
    def __init__(self,name,readQueue,writeQueue):
        super().__init__()
        self.name=name
        self.readQueue=readQueue
        self.writeQueue=writeQueue
    
    def writeMsg(self):
        num=1
        while True:
            if self.writeQueue.qsize()<10:
                self.writeQueue.put(f"{self.name}'s {str(num)}")
                print(f"{self.name} wrote the msg:{self.name}'s {str(num)}")
                num+=1
                sleep(5)
            else:
                num=1
                sleep(5)

    def readMsg(self):
        while True:
            if self.readQueue.qsize()>0:
                print(f"{self.name} have read the msg : {self.readQueue.get()}")
            sleep(2)
    
    def run(self):
        print(f"Process {self.name} is running")
        Thread(target=self.readMsg,name=f"{self.name}--reader").start()
        Thread(target=self.writeMsg,name=f"{self.name}--writer").start()


if __name__=="__main__":
    firstQueue=Queue()
    secondQueue=Queue()
    p1=MyProcess("zhangsan",firstQueue,secondQueue)
    p2=MyProcess("lisi",secondQueue,firstQueue)
    p1.start()
    p2.start()