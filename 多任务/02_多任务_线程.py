import time 
import threading


def miao():
    """喵喵 5秒钟"""
    for i in range(5):
        print("---喵喵喵---")
        time.sleep(1)


def wang():
    """汪汪 5秒钟"""
    for i in range(5):
        print("---汪汪汪---")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=miao)
    t2 = threading.Thread(target=wang)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()