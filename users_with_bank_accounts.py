class BankAccount:
  
  def __init__(self, int_rate, balance):
    self.int_rate=int_rate
    self.balance=balance
  
  def deposit(self, amount):
    self.balance+=amount
    return self
  def withdraw(self, amount):
    if self.balance>amount:
      self.balance-=amount
    else:
      print("Insufficient funds: Charging a $5 fee")
      self.balance-=5
    return self
  def display_account_info(self):
    print(f"Balance: ${self.balance}")
    return self
  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.balance * self.int_rate
    return self
  

class User:
    def __init__(self,name,accounts):
      self.name=name
      self.accounts={}
      
    def add_account(self, account_name, int_rate, balance):
      self.accounts[account_name] = BankAccount(int_rate, balance)
      return self
    def make_deposit (self, amount):
      self.balance+=amount
      print(f"user:{self.name} ,Deposit:${amount} ,Balance:${self.balance}")
      return self
    
    def make_withdrawal(self, amount):
      self.balance-=amount
      print(f"user:{self.name} ,withdrawal:${amount} ,Balance:${self.balance}")
      return self
    
    def display_user_balance(self):
      print(f"user:{self.name} ,Balance:${self.balance}")
      return self
    
    def transfer_money(self, other_user, amount):
      self.other_user=other_user
      self.amount=amount
      if amount<=self.balance:
        self.balance-=amount
        other_user.balance+=amount
        print(f"Transfer to user:{other_user.name} ,Balance:${other_user.balance} My account {self.name} ,Balance:${self.balance}" )
      else:
        print(f"Available balance: ${self.balance}")
      return self
