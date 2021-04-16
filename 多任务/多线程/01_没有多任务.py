import time


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
    miao()
    wang()


if __name__ == "__main__":
    main()