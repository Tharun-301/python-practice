def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 6  # For series till 6th index

for i in range(n + 1):
    print(fib(i), end=", ")




# def fib_term(n):
#      a, b = 0, 1
     
#      for i in range(n+1):
#         yield a
#         a, b = b, a + b
   
# num = 10
# for term in fib_term(num):
#     print(term, end=', ')