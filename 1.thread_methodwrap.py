from threading import Thread
from time import sleep

def func1(name):
    for i in range(3):
        print(f"{name}: {i}")
        sleep(1)

if __name__ == "__main__":
    print("main thread start")
    t1=Thread(target=func1,args=("thread1",))
    t2=Thread(target=func1,args=("thread2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main thread end")
