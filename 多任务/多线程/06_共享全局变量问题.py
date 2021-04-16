#  资源竞争
import threading
import time


g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("--------in test1 g_num = %d" % g_num) 


def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("--------in test2 g_num = %d"% g_num)


def main():
    # target指定将来，这个线程去哪个函数执行
    # args指定函数执行时传递的参数
    t1 = threading.Thread(target = test1, args=(1000000,))
    t2 = threading.Thread(target = test2, args=(1000000,))
    # 共享全局变量，资源竞争g_num，两个共同对g_num进行改写，但其中一个线程进行的时候，对+1还未执行完的时候，时间片用完，中间
    # 结果存储，接下来另一个线程运行，运行完后，g_num已经加完了，但转到另一个线程执行时，他会将之前的中间结果读取出来，进行执行，这样
    # 加起来的数就会变小,相当于一个线程的时间片运行浪费了。

    t1.start()
    t2.start()

    time.sleep(2) # 等待上面线程执行完毕
    print("--------in main g_num = %d" % g_num)


if __name__ =="__main__":
    main()

