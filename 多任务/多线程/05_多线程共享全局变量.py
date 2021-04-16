# 函数中全局变量加global，改变内存地址的时候需加global，如果修改了全局变量的内存地址改变了，必须使用global，如果仅仅修改了原来内存空间中的数据，此时不用必须使用global
# 数字，字符串，元组不可变，必须加global
import threading
import time


g_num = 100


def test1(temp):
    global g_num
    g_num += 1
    temp.append(33)
    print("--------in test1 g_num = %d" % g_num) 
    print("--------in test1 g_nums = %s" % str(temp)) 


def test2(temp):
    print("--------in test2 g_num = %d"% g_num)
    print("--------in test2 g_nums = %s"% str(temp))


ｇ_nums = [11,22]

def main():
    # target指定将来，这个线程去哪个函数执行
    #　args指定函数执行时传递的参数
    t1 = threading.Thread(target = test1, args=(g_nums,))
    t2 = threading.Thread(target = test2, args=(g_nums,))

    t1.start()
    time.sleep(1)
    
    t2.start()
    time.sleep(1)

    print("--------in main g_num = %d" % g_num)


if __name__ =="__main__":
    main()

