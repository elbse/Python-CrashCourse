class BankApp:

    def __init__(self, account, balance =0):
        self.account = account
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
            print(f"Added {amount} to your balance")
        else:
            print("Deposit must be positive amount")

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from your balance")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return print(f"Your balance is {self.__balance}")
    
    print("🏦 Welcome to Python Bank!")
name = input("Enter account owner name: ")
account = BankApp(name)
while True:
    print("\n--- MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdrawal(amount)
    elif choice == "3":
        account.get_balance()
    elif choice == "4":
        print("👋 Thank you for banking with us!")
        break
    else:
        print("❌ Invalid choice. Try again.")