list = [2,4,6,8,10,12,14,16]
print(list[:])
print(list[:5])
print(list[3:7])
print(list[::2])
print(list[2:6:3])
print(list[-1:-5:-1])

#reverse
list = [2,4,6,8,10,12,14,16]
print(list[::-1])
print(list[4:-7:-1])
print(list[-3:2:-1])

#inserting
li = [1,2,3,4,5]
li[5:5] = [6,7,8]
print(li) 

l1 = [1,2,3,4,5]
l1[3:3] = [7,8,9]
print(l1)

# start and stop
l1 = [1,2,3,4,5]
l1[1:4] = [12,24,14]
print(l1)

#start, stop, step
l1 = [1,2,3,4,5]
l1[::2]=[11,12,13]
print(l1)

l1 = [1,2,3,4,5]
l1[::-1] = [11,12,13,14,15]
print(l1)

l1 = [1,2,3,4,5]
l1[3:0:-1]= [11,12,13]
print(l1)

l1 = [1,2,3,5,4,5,6]
l1[4:1:-2] = [2,2]
print(l1)
