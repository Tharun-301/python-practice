# To schedule and execute tasks based on priority, where the highest-priority(smaller numbers) task executed first and lower priority task are executed later using the heapq priority queue.
# heapq is a Python module used to implement a heap (priority queue).
import heapq

class PriorityScheduler:
    def __init__(self):
        self._task_list = [] 

    class Task:
        def __init__(self, name, priority):
            self.name = name
            self.priority = priority

        def __repr__(self):
            return f"Name: {self.name}"

    def add_task(self, name, priority):
        task = self.Task(name, priority)
        heapq.heappush(self._task_list,(priority, task))    

    def next_task(self):
        if self._task_list:
            return heapq.heappop(self._task_list)  #heappop() removes smallest priority task.
            
    def peek_task(self):
        if self._task_list:
            return self._task_list[0]

scheduler = PriorityScheduler()  

scheduler.add_task("Update Website", priority=2)
scheduler.add_task("Update Inventory", priority=1)   
scheduler.add_task("Send Emails", priority=3)   

print("Next task (peek):", scheduler.peek_task())

print("Executing:", scheduler.next_task())
print("Executing:", scheduler.next_task())
print("Executing:", scheduler.next_task())