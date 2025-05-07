from threading import Thread,Event
from time import sleep

def chihuoguo(name):
    print(f"{name} 准备吃火锅...")
    event.wait()
    print(f"{name} 开始吃火锅...")


if __name__=="__main__":
    print("main thread start")
    event=Event()
    t1=Thread(target=chihuoguo,args=("张三",))
    t2=Thread(target=chihuoguo,args=("李四",))
    t1.start()
    t2.start()
    print("主线程等待5秒...")
    sleep(5)
    print("主线程设置事件...")
    event.set()
    t1.join()
    t2.join()
    print("main thread end")

