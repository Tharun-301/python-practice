# dict_a = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
# print(type(dict_a))
# print(dict_a)

# dict_b = {"Name":"Tharun", "age": 21, "roll_no":27}
# print(dict_b)

'''#Creating Empty Dictionary
dict_a = dict()
print(type(dict_a))
print(dict_a)

dict_a = {}
print(type(dict_a))
print(dict_a)'''

'''#Accessing Items
dict_b = {"Name":"Tharun", "age": 21, "roll_no":27}
print(dict_b["Name"])
print(dict_b["age"])

#Accessing Items - Get
dict_b = {"Name":"Tharun", "age": 21, "roll_no":27}
print(dict_b.get("Name"))
print(dict_b.get("city"))'''

# #key Error
# dict_b = {"Name":"Tharun", "age": 21, "roll_no":27}
# print(dict_b["city"])

#Membership check
dict_b = {"Name":"Tharun", "age": 21, "roll_no":27}
result = "Name" in dict_b
print(result)
