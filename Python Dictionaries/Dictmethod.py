#Update the dictionaries
dict_a = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
dict_b = {5:"five"}
dict_a.update(dict_b)
print(dict_a)

#fromkeys
list = [1,2,3,4,5]
dict_a = dict.fromkeys(list)
dict_new = dict.fromkeys(list,"unknown")
print(dict_a)
print(dict_new)

#copy method(shallow copy)
dict_a = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
dict_c = dict_a.copy()
print(dict_c)

dict_a = {"Name": "Tharun","age":21,"city":"Hyderabad"}
dict_b = dict_a.copy()
dict_b["age"] = 27
print(dict_a)
print(dict_b)
print(id(dict_a))
print(id(dict_b))

#pop- Method
dict_a = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
value = dict_a.pop(2)
print(value)
print(dict_a)

missing_value = dict_a.pop(5,'missing')
print(missing_value)

dict_b = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
item = dict_b.popitem()
print(item)
print(dict_b)

#clear method
dict_a = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
dict_a.clear()
print(dict_a) 