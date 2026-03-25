class PaymentMethod:
  def pay(self, amount):
    raise NotImplementedError("Subclasses must implement this method.")
  
class CreditCard(PaymentMethod):
  def pay(self, amount):
    print(f"Paid {amount:.2f} using Credit Card.")

class PayPal(PaymentMethod):
  def pay(self, amount):
    print(f"Paid {amount:.2f} using PayPal.")

class Crypto(PaymentMethod):
  def pay(self, amount):
    print(f"Paid {amount:.2f} using CryptoCurrency.")

def process_payment(payment_method, amount):
  payment_method.pay(amount)    


if __name__ == "__main__":
  payments = [
    CreditCard(),
    PayPal(),
    Crypto()
  ]
  for method in payments:
     process_payment(method, 100.50)

