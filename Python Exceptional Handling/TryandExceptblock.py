# try:
#     # code that may cause error
# except:
#     # code to run when error happens

def div(a, b):
    if b != 0:
        c = a // b
        return c
    else:
        raise ZeroDivisionError
try:
    res = div(10, 0)
    print(res)
except:
    print('Division by Zero')

#User input mistakes
try:
    age = int(input("Enter your age: "))
    print("Your age:", age)
except ValueError:
    print("Please enter only numbers!")

#Dividing numbers
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")

#File operations
# # try:
#     f = open("data.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found!")
    
