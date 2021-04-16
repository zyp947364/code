import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm" +self.name +"@"+str(i)
            print(msg)


if __name__ == "__main__":
    t = MyThread()
    t.start()   # start会自动调用run方法，和Thread(target=函数名)一样

    