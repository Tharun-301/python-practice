class Employee:
  def work(self):
    print("Employee Works")

class Manager(Employee):
  def work(self):
    super().work() # we can call the parent class
    print("Manager manages team") #overriding

class Developer(Employee):
  def work(self):
    print("Developer writes code")

m = Manager()
d = Developer()

m.work()
d.work()