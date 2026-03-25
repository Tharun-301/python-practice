def myrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

m = myrange(4)
print(next(m))  # 0
print(next(m))  # 1
print(next(m))  # 2
print(next(m))  # 3

#Generator Cycling Through Days of the Week
def days():
    d = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    i = 0
    while True:
        yield d[i]
        i = (i + 1) % 7

day_generator = days()
print(next(day_generator))  # Sun
print(next(day_generator))  # Mon
print(next(day_generator))  # Tue

#Generator for even numbers
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

g = even_numbers(10)
for x in g:
    print(x) #Output: 0 2 4 6 8
