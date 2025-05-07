from queue import Queue
from threading import Thread
from time import sleep

def producer(name:str):
    num=1
    while True:
        if  queue.qsize()<5:
            print(f"{name}生产了{num}个馒头")
            queue.put(num)
            num+=1
        else:
            sleep(1)
            print(f"馒头已满。。。一共{num}个")

def consumer(name:str):
    while True:
        queue.get()
        print(f"{name}吃了一个馒头")
        sleep(1)

if __name__=="__main__":
    print("main thread start...")
    queue=Queue(maxsize=5)
    Thread(target=producer,args=("俺是生产者",)).start()
    Thread(target=consumer,args=("消费者张三",)).start()
    Thread(target=consumer,args=("消费者李四",)).start()
    print("main thread end...")

