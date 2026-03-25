#using list.index( ) with default start and end
l1 = [10,20,30,10,20,20,30]

print(l1.index(20)) #searches entire list, output:1
print(l1.index(20,2))#start searches at index 2, out: 4
#print(l1.index(20,2,4))#searches index 2 up to 3, throws the value error


#using list.pop() with arguments:
l2 = [1,2,3,4,5]

print(l2.pop()) #removes last element, op:5
print(l2.pop(1))#removes element at index 1, op: 

#defining a function with default arguments
def volume(l=1,b=1,h=1):
  vol = l*b*h
  return vol
print(volume(10,5,3)) #output: 150
print(volume(10,5)) #h defaults to 1, output:50
print(volume()) # all default 1s, output:1


#individual default arguments types and replacing defaults
def func(a = 12.5,b=25,c="hello"): #they are default values
  print(a,b,c)
func() #op: 12.5 25 hello
func(5,10,15) #op: 5 10 15
func(5,10,[10,11]) #op: 5 10 [10, 11]
func((5,10),{1,2},[10,11]) #op: (5, 10) {1, 2} [10, 11]

#mutable default argument pitfall:
def func(l = [1,2,3]):
  l.append(len(l))
  print(l)

func() #op:[1, 2, 3, 3]
func() #op:[1, 2, 3, 3,4]
func([10,11]) #op:[10, 11, 2]
func() #op:[1, 2, 3, 3,4,5]

