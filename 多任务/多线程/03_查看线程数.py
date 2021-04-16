import threading
import time


def test1():
    for i in range(5):
        print("........test1....%d..." % i)
        time.sleep(1)

def test2():
    for i in range(10):
        print("........test2....%d..." % i)
        time.sleep(1)


def main():
    # # 线程执行的顺序不确定,可以设置适当的延迟来保证某些线程先进行
    # t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)

    # t1.start()
    # time.sleep(1)
    # print("--1--")

    # t2.start()
    # time.sleep(1)
    # print("--2--")
    
    # print(threading.enumerate())


    # # 循环查看当前运行的线程 如果创建ｔｈｒｅａｄ时执行的函数运行结束，那么这个子线程就结束了
    # t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)

    # t1.start()
    # t2.start()
    
    # while True:

    #     print(threading.enumerate())
    #     time.sleep(1)
    #     if len(threading.enumerate()) <= 1:
    #         break 
    
    
    # 验证线程创建时间　当调用ｔｈｒｅａｄ时不会创建线程，当调用实例对象的ｓｔａｒｔ方法的时候才会创建线程以及线程开始运行
    print(threading.enumerate(),"01")
    t1 = threading.Thread(target=test1)

    print(threading.enumerate(), "02")
    t1.start()
    
    print(threading.enumerate(),"03")
    

if __name__ == "__main__":
    main()