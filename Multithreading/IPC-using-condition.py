# A Condition allows one thread to wait until another thread notifies it.
import threading
import time

condition = threading.Condition()
data = None

def producer():
    global data
    with condition:
        print("Producing data...")
        data = "Important Data"
        condition.notify()

def consumer():
    with condition:
        condition.wait()
        print("Consumed:", data)

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
time.sleep(1)
t2.start()