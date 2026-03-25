def is_strong(password):
  msg = "Password must contain atleast "
  if len(password)<8:
    return False, msg + '8 characters.'
  # 
  has_upper = any(c.isupper( )for c in password)
  has_lower = any(c.islower() for c in password)
  has_digit = any(c.isdigit() for c in password)
  special_char = set("!@#$%^&*-_+=")
  has_specia_char = any(c in special_char for c in password)

  if not has_upper:
    return False, msg + "one upper case."
  if not has_lower:
    return False, msg + "one lower case."
  if not has_digit:
    return False, msg + "one or two digits."
  if not has_specia_char:
    return False, msg + "one special char (!@#$%^&*-_+=)"
  
  return "Password is strong!"
password = input('Enter the password🔒: ')
message = is_strong(password)
print(message)