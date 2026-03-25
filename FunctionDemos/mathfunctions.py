#absolute functions - abs(x,/)
print(abs(-70))
print(abs(-70.12))
print(abs(3+4j))

#power function - pow(base,exp,mod=None,/) 
print(pow(2,3))
print(pow(10,2))
print(pow(10,-2))# if negative means goes into denominator 1/100
print(pow(10,2,3)) #100 % 3 = 1, modulus

#round function - round(number,ndigits = None)
#But in banker's rounding, numbers ending in .5 round to the nearest EVEN number.

print(round(4.4))# 4 (because 4 is even)
print(round(4.6))# 5
print(round(4.5))# 4
print(round(5.5))#6
print(round(3.54321))# 4
print(round(3.54321,2))#3.54
print(round(9734,-1)) #9730 (round to nearest one)
print(round(9734,-2))#9700 (round to nearest hundreds)

#divmod function - divmod(a,b) a = quotient, b = reamainder, gives u in tuple
print(divmod(10,3))# 3 = quotient, 1 = reamainder
print(divmod(61,7))# 8 = quotient, 5 = reamainder

#min(iterable,*,key = None,default = None)
numbers = [-10,3,7,-2,-5]
print(min(numbers))
print(min(numbers,key=abs))
print(min([],default="Empty"))

#max(iterable,*,key = None,default = None)
words = ["apple","Banana","cat","Dog"]
print(max(words,key=len))

#sum(iterable,start = 0,/)
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5],start = 20))

#eval(expressions,global = None,local = None)
global_dict = {"x":10,"y":12}
local_dict = {"z":6}
exp = "x+y+z"
print(eval(exp,global_dict,local_dict))
