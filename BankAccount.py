class BankAccount:
    def __init__(self, owner, pin,account_number, balance = 0):
        self.owner = owner
        self.__pin = pin 
        self.account_number = account_number
        self.__balance = balance 
        
    def deposit(self, amount):
        if amount > 0: 
            self.__balance += amount
            print(f"Deposited {amount} to your account")
        else: 
            print("Positive balance only")
        
    def withdrawal(self, amount):
        if amount > 0 and amount <= self.__balance: 
            print(f"Withdrewal with an amount of {amount} is successful")
        else: 
            print("Insufficient balance or invalid amount.")
            
    def check_balance(self):
        return (f"Your remaining balance is {self.__balance}")
        
    def verify_pin(self, pin):
        return pin == self.__pin
        
        
    def get_data(self):
        return(f"{self.account_number}, {self.owner}, {self.pin}, {self.__balance} ")
  


def find_account(account_number, accounts):
    for acc in accounts:
        if acc.account_number == account_number:
            return acc
    return None


# --- Main Program ---
accounts = []
print("🏦 Welcome to Python Bank (In-Memory Version)!")

while True:
    print("\n--- MAIN MENU ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Show All Accounts (Admin View)")
    print("4. Exit")

    choice = input("Choose an option: ")

    # ✅ Create new account anytime
    if choice == "1":
        owner = input("Enter your name: ")
        pin = input("Set a 4-digit PIN: ")
        acc_num = str(1000 + len(accounts) + 1)
        new_acc = BankAccount(owner, pin, acc_num)
        accounts.append(new_acc)
        print(f"✅ Account created successfully! Your account number is {acc_num}")

    # ✅ Login
    elif choice == "2":
        acc_num = input("Enter account number: ")
        acc = find_account(acc_num, accounts)
        if acc:
            pin = input("Enter your PIN: ")
            if acc.verify_pin(pin):
                print(f"\n👋 Welcome back, {acc.owner}!")
                while True:
                    print("\n--- ACCOUNT MENU ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Create New Account")
                    print("5. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == "1":
                        amount = float(input("Enter deposit amount: "))
                        acc.deposit(amount)
                    elif user_choice == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        acc.withdrawal(amount)
                    elif user_choice == "3":
                        print(acc.check_balance())
                    elif user_choice == "4":
                        owner = input("Enter new account owner name: ")
                        pin = input("Set a 4-digit PIN: ")
                        acc_num = str(1000 + len(accounts) + 1)
                        new_acc = BankAccount(owner, pin, acc_num)
                        accounts.append(new_acc)
                        print(f"✅ New account created! Account number: {acc_num}")
                    elif user_choice == "5":
                        print("👋 Logged out successfully.")
                        break
                    else:
                        print("❌ Invalid choice.")
            else:
                print("❌ Incorrect PIN.")
        else:
            print("❌ Account not found.")

    # ✅ Show all existing accounts (for testing)
    elif choice == "3":
        print("\n📋 All Active Accounts:")
        if accounts:
            for acc in accounts:
                print(f"- {acc.account_number}: {acc.owner}")
        else:
            print("No accounts yet. Create one first!")

    # ✅ Exit the program
    elif choice == "4":
        print("👋 Thank you for banking with us!")
        break

    else:
        print("❌ Invalid choice.")