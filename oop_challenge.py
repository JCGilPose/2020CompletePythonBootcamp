class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return (f"Account owner:   {self.owner}\nAccount balance: ${self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")

# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
