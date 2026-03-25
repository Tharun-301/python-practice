import time


class Stopwatch:

    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0

    def start(self):
        if self._start_time is None:
            self._start_time = time.time()
            print("Stopwatch started")
        else:
            print("Stopwatch is already running")

    def stop(self):
        if self._start_time is not None:
            elapsed = time.time() - self._start_time
            self._elapsed_time += elapsed
            self._start_time = None
            print("Stopwatch stopped")
        else:
            print("Stopwatch is not running")

    def reset(self):
        self._start_time = None
        self._elapsed_time = 0
        print("Stopwatch reset")

    def get_elapsed_time(self):
        if self._start_time is not None:
            return self._elapsed_time + (time.time() - self._start_time)
        return self._elapsed_time

    def display_time(self):
        elapsed = self.get_elapsed_time()
        print(f"⏱ Elapsed Time: {elapsed:.2f} seconds")


sw = Stopwatch()

while True:

    print("\n------ Stopwatch Menu ------")
    print("1. Start")
    print("2. Stop")
    print("3. Reset")
    print("4. Show Time")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        sw.start()

    elif choice == "2":
        sw.stop()

    elif choice == "3":
        sw.reset()

    elif choice == "4":
        sw.display_time()

    elif choice == "5":
        print("Exiting stopwatch...")
        break

    else:
        print("Invalid choice")