#all positional and keyword arguments

def func(a,b,c,d):
  print(a,b,c,d)

func(5,6,7,8)
func(a=5,b=6,c=7,d=8)

#function with position-only arguments indicated by slash

def fun(a,b,/,c,d):
  print(a,b,c,d)

fun(5,10,c=2,d=7)  #a, b are positional-only c,d are keyword allowed
fun(5,10,2,7) #all postional allowed
#fun(a=5,b=10,c=2,d=7) #Type Error a and b must be positional arguments

def fun(a,b,c,d,/):
  print(a,b,c,d)

fun(5,6,7,8)
#fun(a=5,b=6,c=7,d=8)#TypeError: fun() got some positional-only arguments passed as keyword arguments: 'a, b, c, d'

# def fun(/,a,b,c,d):#SyntaxError: at least one argument must precede /
#   print(a,b,c,d)

# fun(5,6,7,8)