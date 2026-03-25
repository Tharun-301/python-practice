class NegativeAgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    
    print("Your age is:", age)

except NegativeAgeError as e:
    print(e)
