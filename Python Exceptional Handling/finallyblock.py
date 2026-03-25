#finally block always runs, whether error happens or not.
# finally → always runs
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print("Program finished")#Even though there is an error, finally still executes.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print("Program finished")
