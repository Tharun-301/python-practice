#check prime numbers
def is_prime(number):
    no_of_factors = 0
    
    for i in range(1, number + 1):
        if (number % i == 0):
            no_of_factors += 1
        
    if no_of_factors == 2:
        return "Prime Number"
    else:
        return "Not a Prime Number"

number = int(input('Enter the prime numbers: '))
result  = is_prime(number)
print(result)

#prime numbers n=8, from 1to8---2,3,5,7

def is_prime(n):

    for x in range(2,n+1):
        isprime = True

        for i in range(2,x):
            if x%i==0:
                isprime = False
                break
        if isprime:
            print(x, end=" ")   


n = int(input('Enter the number: ')) 
is_prime(n)