def func(*args):

  print(args)

func(10,15.23,True,'Hell0')  

#without tuple
def func(*args):

  for x in args:
    print(x)

func(10,15.23,True,5,'Hello')  

#only integers
def func(*args):

  for x in args:
    if type(x) == int:
      print(x)

func(10,15.23,True,'Hell0',5) 

#positional
def func(a, b, *args):

  print(a,b,args)#it follows only positional args not keyword before '*'args

func(10,20,30,40,50)  

#keyword
def func(*args,a,b):

  print(a,b,args)#a and b must be pass keyword agrs only after '*'args

func(10,20,30,a= 40,b = 50)  

#list values
def func(*args):
  print(args,len(args))

l1= [10,20,30]
func(l1)#it takes tuple as single value
func (*l1) #it takes individual  values

