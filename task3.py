class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ₱{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₱{amount}. New balance: ₱{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account Balance: ₱{self.balance}")

# Creating a bank account
account = BankAccount("12345678", "Charmaine Villanueva", 1000.0)

while True:
    print("\nBank Account Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        account.deposit()
    elif choice == "2":
        account.withdraw()
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
