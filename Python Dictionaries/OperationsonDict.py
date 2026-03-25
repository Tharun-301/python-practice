#Adding key value pair
dict_a =  {"Name":"Tharun", "age": 21}
dict_a['city'] = "Hyderabad"
dict_a["sports"] = "Cricket"
print(dict_a)

#modifying existing item
dict_a = {"Name":"Jason", "age" : 21}
dict_a["age"] = 22
print(dict_a)

#Deleting an existing item
dict_a = {"Name":"Jason", "age" : 21, "city":"Hyderabad"}
del dict_a["age"]
print(dict_a)

dict_a = {"Name":"Jason", "age" : 21}
print(len(dict_a))  # length of dict_a
if 'Name' in dict_a:  # Membership Check 
    print("True")
dict_a.clear()  # clearing dict_a
print(dict_a)

#iterating
dict_a = {'name': 'Teja', 'age': 15}
for k in dict_a.keys():
    if k == 'name':
        del dict_a[k]
print(dict_a)