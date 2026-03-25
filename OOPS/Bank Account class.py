class InsufficientFundsError(Exception):
  pass

class BankAccount:
  acc_counter = 100

  def __init__(self,name,balance):
    BankAccount.acc_counter += 1
    self.__account = BankAccount.acc_counter
    self.name = name
    self.__balance = balance

  def deposit(self, amount):
    self.__balance += amount  

  def withdraw(self, amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount 
    else:
      raise InsufficientFundsError("Not enougth funds") 
    
  def get_balance(self):
    return self.__balance
  
  def details(self):
    return self.name, self.__account, self.__balance
  

name  = input('Enter account holder name: ')
balance =  float(input('Enter intial balance: '))

account = BankAccount(name, balance)
print("Account created successfully!")
print(account.details())

amount = float(input('Enter deposit amount: '))
account.deposit(amount)

amount = float(input("Enter withdraw amount: "))
try:
  account.withdraw(amount)
except InsufficientFundsError as e:
  print(e)

print("Final Balance:",account.get_balance())    