# A mutex lock prevents multiple threads from accessing shared data simultaneously.
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter:", counter)