import multiprocessing
from multiprocessing import Queue


def test1(q):
    data = [11,22,33,44]

    for temp in data:
        q.put(temp)
    print("-----传输完毕")


def test2(q):
    data = []
    while(True):
        data.append(q.get())
        if q.empty():
            break


def main():
    q = Queue()
    
    p1 = multiprocessing.Process(target=test1, args=(q,))
    p2 = multiprocessing.Process(target=test2, args=(q,))
    p1.start()
    p2.start()


if __name__ =="__main__":
    main()