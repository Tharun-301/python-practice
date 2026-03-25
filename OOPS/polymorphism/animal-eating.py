class Cow:
    def eat(self):
        print("Cow eats grass")

class Lion:
    def eat(self):
        print("Lion eats meat")

def animals(food):
    food.eat()

food = Cow()
animals(food)  
food = Lion()
animals(food)