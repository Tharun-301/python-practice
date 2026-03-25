def validate_atm_pin_code(pin):
  length = len(pin)             #find the length of the pin
  is_valid_len = (length == 4) or (length == 6)  #It is valid if the pin is 4 or 6
  are_digits = pin.isdigit()        #Check if the pin is digit   
  if is_valid_len == True and are_digits == True:  #if both the conditions are valid print "Valid PIN Code" and Else, "Invalid PIN Code".
    return "Valid PIN Code"
  else:
    return "Invalid PIN Code"
  
pin = input('Enter the pin: ')
msg = validate_atm_pin_code(pin)
print(msg)  