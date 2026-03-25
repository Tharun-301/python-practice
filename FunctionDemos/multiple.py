def func(a,b,c):

  sum = a+b+c
  prod = a*b*c

  return sum, prod

print(func(5,4,2))


def result(mark1,mark2,mark3):

  total = mark1+mark2+mark3
  avg = total/3
  if avg >= 45:
    grade = 'pass'
  else:
    grade = 'fail'
  return total,avg,grade
print(result(55,56,72))    