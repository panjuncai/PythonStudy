from multiprocessing import Pipe,current_process,Process
from time import sleep
from multiprocessing.connection import Connection
from multiprocessing.process import BaseProcess

def func1(conn1: Connection) -> None:
    sub_info: str = "hi there"
    print(f"process1-- {current_process().pid} send data:{sub_info}")
    sleep(1)
    conn1.send(sub_info)
    print(f"I am conn1,data from process2:{conn1.recv()}")

def func2(conn2: Connection) -> None:
    sub_info: str = "hello can I help you?"
    print(f"process2-- {current_process().pid} send data:{sub_info}")
    sleep(1)
    conn2.send(sub_info)
    print(f"I am conn2,data from process1:{conn2.recv()}")


if __name__=="__main__":
    print("main process start")
    conn1,conn2=Pipe()
    p1: BaseProcess = Process(target=func1,args=(conn1,))
    p2: BaseProcess = Process(target=func2,args=(conn2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("main process end")
