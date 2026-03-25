
# item1, price1 = 'Pop corn ', ' $20'
# item2, price2 = 'Burger ', ' $35'
# item3, price3 = 'Pizza ', ' $50'
# item4, price4 = 'Cool drink ', ' $10'

# print(item1 + '-' * (20 - len(item1 + price1)) + price1)
# print(item2 + '-' * (20 - len(item2 + price2)) + price2)
# print(item3 + '-' * (20 - len(item3 + price3)) + price3)
# print(item4 + '-' * (20 - len(item4 + price4)) + price4)

#using for loop
item1, price1 = 'Pop corn ', ' $20'
item2, price2 = 'Burger ', ' $35'
item3, price3 = 'Pizza ', ' $50'
item4, price4 = 'Cool drink ', ' $10'

for item, price in ((item1, price1),(item2,price2),(item3,price3),(item4, price4)):
  print(item + '-'* (20-(len(item + price)))+ price)

