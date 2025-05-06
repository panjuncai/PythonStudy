from threading import Thread,Lock
from time import sleep

def fun1():
    lock1.acquire()
    print("fun1 获取了lock1")
    sleep(2)
    lock2.acquire()
    print("fun1 获取了lock2")
    sleep(2)
    lock2.release()
    print("fun1 释放了lock2")
    lock1.release()
    print("fun1 释放了lock1")

def fun2():
    lock2.acquire()
    print("fun2 获取了lock2")
    sleep(2)
    lock1.acquire()
    print("fun2 获取了lock1")
    sleep(2)
    lock1.release()
    print("fun2 释放了lock1")
    lock2.release()
    print("fun2 释放了lock2")

if __name__=="__main__":
    print("main thread start")
    lock1=Lock()
    lock2=Lock()
    t1=Thread(target=fun1)
    t2=Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main thread end")

