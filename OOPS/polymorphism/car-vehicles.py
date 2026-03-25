class Tesla:
  def drive(self):
    print(" Drive Tesla car")

class Buggati:
  def drive(self):
    print("Drive Buggati car") 

def driver(car):
  car.drive()


car = Buggati()
driver(car)
