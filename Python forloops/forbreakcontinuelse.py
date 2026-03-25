#break is used to stop the loop immediately when a condition is met.
for i in range(1, 10):
    if i == 5:
        break
    print(i)
#continue is used to skip the current iteration and move to the next one.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#else..The else block with a loop runs only if the loop completes normally
for i in range(1, 6):
    print(i)
else:
    print("Loop finished without break")
#The else didn’t run because the loop was stopped with break.
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished without break")
   


