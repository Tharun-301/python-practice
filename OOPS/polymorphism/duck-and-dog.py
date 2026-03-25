class Dog:
  def sound(self):
    print("dog sounds bark")

  def walk(self):
    print("dog walk")  

class Duck:
  def sound(self):
    print("duck sounds Buck")

  def walk(self):
    print("Duck walk")  

def person(pet):
  pet.sound()
  if hasattr(pet,"walk"):
    pet.walk()

dog = Dog()
person(dog)
duck = Duck()
person(duck)  
