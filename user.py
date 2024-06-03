class User:#reem
    def __init__(self,name,balance):
      self.name=name
      self.balance=balance
      
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
    
user1=User("Reem", 400)
user2=User("Jad", 200)
user3=User("Shaden",1000)


user1.make_deposit(20)\
.make_deposit(50)\
.make_deposit(1000)\
.make_withdrawal(500)\
.display_user_balance()
user2.make_deposit(500).make_deposit(1000).make_withdrawal(700).make_withdrawal(600).display_user_balance()
user3.make_deposit(1400).make_withdrawal(500).make_withdrawal(20).make_withdrawal(300).display_user_balance()
user2.transfer_money(user3,400)