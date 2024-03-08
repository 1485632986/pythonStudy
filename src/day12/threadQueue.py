# from multiprocessing import Process, Queue
# from time import sleep
# counter = 0
# def sub_task(string):
#     global counter
#     while counter < 10:
#         print(string, end='', flush=True)
#         counter += 1
#         sleep(0.01)
# def main():
#     Process(target=sub_task, args=('Ping', )).start()
#     Process(target=sub_task, args=('Pong', )).start()
# if __name__ == '__main__':
#     main()

from multiprocessing import Process, Value, Lock
from time import sleep

# 创建一个初始化为0的共享整数值和一把锁
counter = Value('i', 0)
counter_lock = Lock()

def sub_task(counter, counter_lock, string):
    while True:
        with counter_lock:  # 使用锁确保并发安全
            if counter.value < 10:
                print(string, end='', flush=True)
                counter.value += 1  # 原子性增加计数器值
                sleep(0.01)
            else:
                break

def main():
    p1 = Process(target=sub_task, args=(counter, counter_lock, 'Ping'))
    p2 = Process(target=sub_task, args=(counter, counter_lock, 'Pong'))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()
