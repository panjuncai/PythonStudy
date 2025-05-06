from threading import Thread,Lock
from time import sleep

class Account:
    def __init__(self,name,money):
        self.name=name
        self.money=money

class Drawing(Thread):
    def __init__(self,drawingNum:int,account:Account,lock:Lock):
        Thread.__init__(self)
        self.drawingNum=drawingNum
        self.account=account
        self.expenseTotal=0
        self.lock=lock

    def run(self):
        self.lock.acquire()
        if self.account.money-self.drawingNum<0:
            print(f"{self.name}取钱失败，账户余额为{self.account.money}")
            return
        sleep(1)
        self.account.money-=self.drawingNum
        self.expenseTotal+=self.drawingNum
        self.lock.release()
        print(f"{self.name}取钱成功，账户余额为{self.account.money}")
        print(f"{self.name}取钱成功，取钱总数为{self.expenseTotal}")

if __name__=="__main__":
    print("main thread start")
    lock=Lock()
    account=Account("张三",1000)
    drawing1=Drawing(500,account,lock)
    drawing2=Drawing(800,account,lock)
    drawing1.start()
    drawing2.start()
    drawing1.join()
    drawing2.join()
    print("main thread end")

