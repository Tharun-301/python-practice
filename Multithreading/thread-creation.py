# Using Thread class
import threading

def task():
    print("Thread is running")

t = threading.Thread(target=task)
t.start()
t.join()

# Extending the Thread class
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Thread created using class")

t = MyThread()
t.start()
t.join()