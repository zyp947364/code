# 当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制

# 线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。

# 互斥锁为资源引入一个状态：锁定/非锁定

# 某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；
# 直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。
# 互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
#  资源竞争
import threading
import time


g_num = 0


def test1(num):
    global g_num
    # 上锁，如果之前没有被锁，那么上锁成功，
    # 如果之前已被锁，那么堵塞在这里，知道锁解开
    # mutex.acquire()
    # for i in range(num):
    #     g_num += 1
    # # 解锁
    # mutex.release()
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("--------in test1 g_num = %d" % g_num) 


def test2(num):
    global g_num
    # mutex.acquire()
    # for i in range(num):
    #     g_num += 1
    # # 解锁
    # mutex.release()
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("--------in test2 g_num = %d"% g_num)

# 创建一个互斥锁，默认没有上锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target = test1, args=(1000000,))
    t2 = threading.Thread(target = test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(5) # 等待上面线程执行完毕
    print("--------in main g_num = %d" % g_num)


if __name__ =="__main__":
    main()

