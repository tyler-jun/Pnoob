import threading, datetime


# 每隔interval打印当前时间
class MyTimer:
    def __init__(self, interval):
        self.interval = interval

    def intervalPrint(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # 1 global的作用?
        global timer
        # 2 这里调用的intervalPrint, 不是intervalPrint() ----区别很大，intervalPrint()会递归，栈内存溢出
        timer = threading.Timer(self.interval, self.intervalPrint)
        timer.start()


if __name__ == '__main__':
    mt = MyTimer(3)
    mt.intervalPrint()
