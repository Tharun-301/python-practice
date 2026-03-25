#When a recursive function keeps calling itself, calls get stacked on top of each other.
#When the base case is reached, the function starts returning back one by one — this process is called unwinding.
def sum_of_digits(n):
  if n==0:
    return 0 
  else: 
    return (n%10) + sum_of_digits(n//10)
  
n = int(input('Enter the digits: '))
print(sum_of_digits(n))  