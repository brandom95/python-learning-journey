class Account:
    def __init_(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit (self, amount):
        self.balance += amount

    def withdraw (self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("sorry not enought fund")

    def statemente (self
