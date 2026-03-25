emailid = input('Enter the email: ')
atrate = emailid.find('@')
print(atrate)
# user_id = emailid[:atrate]
# print(user_id)
print('user id: ',emailid[:atrate])
print('domain name: ',emailid[atrate+1:])