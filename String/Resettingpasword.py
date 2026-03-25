password1 = input(' new password: ')
password2 = input(' re-new password: ')
if password1 == password2:
  print('Password change')
else:
  if password1.casefold() == password2.casefold():
    print('please check cases and try again')
  else:
    print('Password not change')    