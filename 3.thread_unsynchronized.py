from threading import Thread
from time import sleep

class Account:
    def __init__(self,name,money):
        self.name=name
        self.money=money

class Drawing(Thread):
    def __init__(self,drawingNum:int,account:Account):
        Thread.__init__(self)
        self.drawingNum=drawingNum
        self.account=account
        self.expenseTotal=0

    def run(self):
        if self.account.money-self.drawingNum<0:
            return
        sleep(1)
        self.account.money-=self.drawingNum
        self.expenseTotal+=self.drawingNum
        print(f"{self.name}取钱成功，账户余额为{self.account.money}")
        print(f"{self.name}取钱成功，取钱总数为{self.expenseTotal}")

if __name__=="__main__":
    account=Account("张三",1000)
    drawing1=Drawing(500,account)
    drawing2=Drawing(800,account)
    drawing1.start()
    drawing2.start()
    print("main thread end")

