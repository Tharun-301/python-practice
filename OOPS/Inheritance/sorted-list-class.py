# The goal is to automatically keep the list sorted whenever a value is inserted.
# bisect is a Python module used for binary search and inserting elements in sorted order.
import bisect   

class SortedList:

  def __init__(self):
    self.lst = []

  def add(self,value):
    bisect.insort(self.lst, value)  #insort() inserts the value in the correct sorted position.

  def remove(self, value):
    self.lst.remove(value)  

  def search(self, key):
    return self.lst.index(key)

  def insert_position(self, value):
    position  = bisect.bisect_left(self.lst, value)
    return position

  def display(self):
    print(self.lst)

sl = SortedList()

sl.add(10)
sl.add(1)
sl.add(7)
sl.add(3)
sl.add(6)
sl.add(11)
sl.add(5)
sl.remove(11)
sl.display()
print("Index: ",sl.search(6))
print("position: ",sl.insert_position(8))
