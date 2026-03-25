class InsufficientFundError(Exception):
  pass

def withdrawal(balance, amount):
  if amount > balance:
    raise InsufficientFundError("withdraw amount should be less than balance")
  return balance - amount

balance = 30000 
amount = int(input('Enter the withdraw amount: '))  

try:
  rem_balance = withdrawal(balance,amount)
  print("withdrawal Successfully!")
  print("Remaining balance: ",rem_balance)

except InsufficientFundError as e:
  print(e)  