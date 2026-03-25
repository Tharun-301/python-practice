def func():
  a = 10
  print('local',a)#local variable
func()  


# def func():
#   a = 10
#   print('local',a)
#   print('global',g)#NameError: name 'g' is not defined
# func()
# g = 3.5  


g = 5.2  #global var dec before the func
print('outside-1: ',g)
def func():
  a = 12
  print('local',a)#local variable
  print('global',g) #reading global variables inside the func
func()  
print('outside-2: ',g)


g = 5.2  #global var dec before the func
print('outside-1: ',g)
def func():
  a = 12
  g = 199
  print('local',a)#local variable
  print('global',g) #reading global variables inside the func
func()  
print('outside-2: ',g)#it will not modify global var from inside func

g = 5.25  #global var dec before the func
print('outside-1: ',g)
def func():
  global g
  a = 13
  g = 198
  print('local',a)#local variable
  print('global',g) #reading global variables inside the func
func()  
print('outside-2: ',g)#we can access the outside global var by using global keyword from inside func




x, y, z = 5, 1.25, 'hi' #global

def func():
  a,b,c = 2,5,8  #local
  print("locals",locals())
  print("globals",globals())

func()  
