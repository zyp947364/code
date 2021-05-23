import multiprocessing
import time


def test1():
    global num
    while True:
        num += 1
        print("1---- %d" % num)
        time.sleep(1)


def test2():
    global num
    while True:
        num += 1
        print("2---- %d" % num)
        time.sleep(1)

num = 100
def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    p1.start() # 在此处创建新进程 且主进程拥有什么子进程拥有什么(资源) 进程号pid不同 拥有一样的资源但后续的更改不同
    p2.start() 

if __name__ == "__main__":
    main()
