def fun(**kwargs):
  print(kwargs)

fun(a = 10,b = 15, c = 20)  

def func(**kwargs):
  for item in kwargs.items():
    if item[0]=='b':
      print(item[1])

func(a = 10,b = 15, c = 20)  



def func(a,b,**kwargs):
    print(a,b)
    print(kwargs)

func(a = 10,b = 15,c = 12)


def func(*args,a,b,**kwargs):
  print(args)
  print(a,b)
  print(kwargs)

func(1, 2, 3, a = 4,b = 5, x = 6, y = 7, z = 8 )  

# def func(**kwargs,a,b):#SyntaxError: arguments cannot follow var-keyword argument
#   print(kwargs)

# func(1,2,3)
