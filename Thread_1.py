"""import _thread
import time

def check(NameOfThread, delay):
    count = 1
    while count < 50:
        time.sleep(delay)
        count += 1
        print(NameOfThread,"---------" ,time.time())

_thread.start_new_thread(check,("First_thread",1))
_thread.start_new_thread(check,("Second_thread",1))
_thread.start_new_thread(check,("Third_thread",1))
_thread.start_new_thread(check,("Fourth_thread",1))
_thread.start_new_thread(check,("Fifth_thread",1))"""


import threading
import time

def check(NameOfThread, delay):
    count = 1
    while count < 50:
        time.sleep(delay)
        count += 1
        print(NameOfThread,"---------" ,time.time())

if __name__ == "__main__":
    t1 = threading.Thread(target = check, args= ("Thread_1",1))
    t2 = threading.Thread(target = check, args= ("Thread_2",1))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Finish")







        
