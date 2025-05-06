from threading import Thread, Semaphore
from time import sleep

def home(name:str,sem:Semaphore):
    sem.acquire()
    print(f"{name} 进入房间")
    sleep(2)
    sem.release()
    print(f"{name} 离开房间")

if __name__=="__main__":
    print("main thread start")
    sem=Semaphore(2)
    for i in range(7):
        Thread(target=home,args=(f"thread{i}",sem)).start()
    print("main thread end")