import json

print("Welcome to BankApp V02.0!")

class BankApp:
    def __init__(self, owner, account_number, pin, balance = 0):
        self.owner = owner 
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance 

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to your balance")
        else:
            print("Deposit must be positive amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from your balance")
        else: 
            print("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
            print(f"💰 Your current balance is: {self.__balance:.2f}")

    