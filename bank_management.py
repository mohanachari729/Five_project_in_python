# Parent class for User
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


# Child class for BankAccount
class BankAccount(User):
    def __init__(self, username, password, name, account_number, balance=0):
        super().__init__(username, password)
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount {amount} credited  in your account.")
            print(f" the account balance: {self.balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Amount {amount} debited in your account.")
            print(f" the balance in your account is: {self.balance}")

    def check_balance(self):
        print(f" the total Account Balance: {self.balance}")


# Bank Management System
class BankManagementSystem:
    def __init__(self):
        self.accounts = []  # Stores BankAccount objects

    def create_account(self):
        name = input("Enter your name: ")
        account_number = input("Enter account number: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        # Check if account number or username already exists
        for account in self.accounts:
            if account.account_number == account_number:
                print("Account number already exists!")
                return
            if account.username == username:
                print("Username already exists!")
                return

        # Create new account
        new_account = BankAccount(username, password, name, account_number)
        self.accounts.append(new_account)
        print("Account created successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in self.accounts:
            if account.login(username, password):
                print(f"Welcome, {account.name}!")
                return account
        print("Invalid username or password! please enter currect details")
        return None

    def run(self):
        logged_in_account = None
        while True:
            print("\n===== Bank Management System =====")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            if logged_in_account:
                print("4. Deposit")
                print("5. Withdraw")
                print("6. Check Balance")
                print("7. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                if not logged_in_account:
                    logged_in_account = self.login()
                else:
                    print("You are already logged in!")
            elif choice == "3":
                print("Exiting the system. have a nice day")
                break
            elif choice == "4" and logged_in_account:
                amount = float(input("Enter amount to deposit: "))
                logged_in_account.deposit(amount)
            elif choice == "5" and logged_in_account:
                amount = float(input("Enter amount to withdraw: "))
                logged_in_account.withdraw(amount)
            elif choice == "6" and logged_in_account:
                logged_in_account.check_balance()
            elif choice == "7" and logged_in_account:
                logged_in_account = None1
                
                print("Logged out successfully!")
            else:
                print("Invalid choice! Please try again.")


# Run the Bank Management System
if __name__ == "__main__":
    bank_system = BankManagementSystem()
    bank_system.run()