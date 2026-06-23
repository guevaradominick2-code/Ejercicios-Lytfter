class Bank_Account():

    def __init__(self, balance):
        self.balance = balance

    def deposit_balance(self, amount):
        self.balance += amount

    def withdraw_balance(self, amount):
         self.balance -= amount

class SavingsAccount(Bank_Account):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw_balance(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Insufficient Funds")
        else:
            super().withdraw_balance(amount)

account_1 = SavingsAccount(43750, 20000)

account_1.deposit_balance(56250)
print(account_1.balance)

account_1.deposit_balance(100000)
print(account_1.balance)

account_1.withdraw_balance(75500)
print(account_1.balance)
  
try:
    account_1.withdraw_balance(1145000)
    print(account_1.balance)
except ValueError as ex:
    print(f"Denied: {ex}")   