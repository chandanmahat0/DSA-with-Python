class CreditCard:
  # Declaring Instance Variables:
  def __init__(self, customer, bank, account, balance, limit):
    self._customer = customer
    self._bank = bank
    self._account = account
    self._balance = balance
    self._limit = limit

  def get_customer(self):
    return self._customer # Returns Customer Name
  
  def get_bank(self):
    return self._bank # Return Bank Name
  
  def get_account(self):
    return self._account # Return Account Number
  
  def get_balance(self):
    return self._balance # Return Total Balance in the account
  
  def get_limit(self):
    return self._limit # Return Limit of Credit Card
  
  def charge(self, price):
    if (price + self._balance) > self._limit:
      return False
    else:
      self._balance += price
      return True
    
  def make_payment(self, amount):
    # Process customer payment that reduces balance.
    self._balance -= amount
  
if __name__ == '__main__':
  wallet = []
  wallet.append(CreditCard("John", "Punjab Bank", "2343 4563 0981 7789", 25000, 5000))
  wallet.append(CreditCard("Rahul", "Indian Bank", "3434 4563 8888 7789", 2500, 1000))
  wallet.append(CreditCard("Anand", "SBI Bank", "8888 4563 3434 7789", 5000, 2000))
  wallet.append(CreditCard("Roshan", "Punjab Bank", "3434 4563 0981 8888", 50000, 3000))

  for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2 * val)
    wallet[2].charge(3 * val)

  for c in range(3):
    print("Customer = ", wallet[c].get_customer())
    print("Bank = ", wallet[c].get_bank())
    print("Account = ", wallet[c].get_account())
    print("Limit = ", wallet[c].get_limit())
    print("Balance = ", wallet[c].get_balance())
    while (wallet[c].get_balance() > 5000):
      wallet[c].make_payment(1000)
      print("New Balance = ", wallet[c].get_balance())
    print()
    print("-----------------------------------------------")
    print()