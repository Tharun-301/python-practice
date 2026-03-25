name = 'Jason'
rollNo = 21
avg = 73
print(f'student name is {name} and his rollNo is{rollNo} and avg{avg}.')
# print('student name is {0} and his rollNo is {1} and avg is {2}'.format(name,rollNo,avg))
# print('student name is {name} and his rollNo is {rollNo} and avg is {avg}'.format(name=name,rollNo=rollNo,avg=avg))
data = 25
print('start {0:15} end'.format(data))#it takes width and precision
#flag position- :< , :^ , :> , :+ , :-
print('start {0:^20} end'.format(data))
#conversions  - d,b,f,F,e,E,,o
print('start {0:<15o} end'.format(data))
print('start {0:^15b} end'.format(data))