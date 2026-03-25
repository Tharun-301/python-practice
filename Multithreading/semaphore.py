# A semaphore controls how many threads can access a resource simultaneously.
import threading
import time

semaphore = threading.Semaphore(2)

def access_resource(name):
    semaphore.acquire()
    print(f"{name} entered")
    time.sleep(2)
    print(f"{name} leaving")
    semaphore.release()

for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread-{i}",))
    t.start()