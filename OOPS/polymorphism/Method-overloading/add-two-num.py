class Add:
  def sum(self, a, b, c = 0):
    print("sum: ",a + b + c)

obj = Add()

obj.sum(5,7)
obj.sum(5,4,6)