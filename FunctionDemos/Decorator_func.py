def decorator(f):
  def inner():
    print("+"*10)
    f()
    print("+"*10)
  return inner

@decorator
def display():
  print('Welcome')

display()    