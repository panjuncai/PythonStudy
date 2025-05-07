from multiprocessing import Process
import os
from time import sleep

def func1(name:str):
    print(f"current process is {os.getpid()}")
    print(f"current's parent process is {os.getppid()}")
    print(f"Process {name} starts")
    sleep(1)
    print(f"Process {name} ends")

if __name__=="__main__":
    Process(target=func1,args=("zhangsan",)).start()
    Process(target=func1,args=("lisi",)).start()