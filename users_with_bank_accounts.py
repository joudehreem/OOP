from bankaccount import BankAccount
class User:
    def __init__(self,name):
      self.name=name
      self.account=BankAccount(14,5000)
    def create_account(self,account_type):
      self.account_type=account_type
    def make_deposit (self, amount):
      self.account.deposit(amount)
      print(f"user:{self.name} ,Deposit:${amount} ,Balance:${self.account.balance}")
      return self
    def make_withdrawal(self, amount):
      self.account.withdraw(amount)
      print(f"user:{self.name} ,withdrawal:${amount} ,Balance:${self.account.balance}")
      return self
    def display_user_balance(self):
      print(f"user:{self.name} ,Balance:${self.account.balance}")
      return self
    def transfer_money(self, other_user, amount):
      if amount<=self.account.balance:
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        print(f"Transfer to user:{other_user.name} ,Balance:${other_user.balance} My account {self.name} ,Balance:${self.account.balance}" )
      else:
        print(f"Available balance: ${self.account.balance}")
      return self
    def yield_interest(self):
      self.account.yield_interest()
      return self
user1=User("Reem")
user1.make_deposit(20)\
.make_deposit(50)\
.make_deposit(1000)\
.make_withdrawal(500)\
.yield_interest()\
.display_user_balance()

user2=User("jad")
user2.make_deposit(20000)\
.make_deposit(500)\
.make_deposit(100000)\
.make_withdrawal(500)\
.yield_interest()\
.display_user_balance()
