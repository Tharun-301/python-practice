#keys() , values() & items() are called Dictionary Views as they provide a dynamic view on the dictionary’s items.
#keys
dict_a = {"Name":"Tharun","age":21}
print(dict_a.keys())

#values
dict_a = {1:"one",2:"two",3:"third",4:"four"}
print(dict_a.values()) 

#items
dict_a = {"Name":"Tharun","age":21}
print(dict_a.items())

#Iterate over Dictionary Views
#Example - 1
dict_a = {"Name":"Tharun","age":21}

for key in dict_a.keys():
  print(key)

#Example - 2
dict_a = {"Name":"Tharun","age":21}

key_list = list(dict_a.keys())
print(key_list)

#Example - 3
dict_a = {"Name":"Tharun","age":21}

for value in dict_a.values():
  print(value)

#Example - 4
dict_a = {"Name":"Tharun","age":21}  

for key, value in dict_a.items():
  pair = "{} {}".format(key,value)
  print(pair)

# Example - 5
dict_a = {"Name":"Tharun","age":21} 

view = dict_a.keys()
print(view)
dict_a["city"] = "Hyderabad"
print(view)

#list to dictionaries
list_a = [("Name","Tharun"),("age",21),("city","Hyderabad")]

dict_a = dict(list_a)
print(dict_a)

list_b = ["Name","age",21]
dict_a = dict(list_b)
print(dict_a)