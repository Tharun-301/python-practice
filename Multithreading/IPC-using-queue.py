# A queue is the safest way for threads to communicate.
import threading
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        print("Producing", i)
        q.put(i)

def consumer():
    for i in range(5):
        item = q.get()
        print("Consumed", item)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()