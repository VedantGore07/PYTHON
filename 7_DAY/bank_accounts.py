# Q1. Create a class called BankAccount with a constructor that takes initial_amount, acct_name as a parameter. 
# create a function called get_balance which will display the balance amount( initial time it will initial_amount as a balance),
#  create a function called deposit which accepts amount as a argument. create a function called Viable_transaction which will check balance
#  amount before withdrawal of amount (if balance greater that or equal to amount which return nothing, else raise BalanceException displaying 
# "Sorry account only has a balance amount :{self.balance:.2f}")

# create a function called withdraw which accepts amount as a argument.withdraw functions calls the viable_transaction(amount) else display 
# the error message. Save the program as "bank_accounts.py", create another program oops.py in this program "from bank_accounts import *" create a 
# object for BankAccount and access all the methods like get_balance, deposit, withdraw.

# class BalanceException(Exception):
#     pass

# Include this code beginning of the file "bank_accounts.py"



class BalanceException(Exception):
    pass


class BankAccount:

    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.acct_name = acct_name

    def get_balance(self):
        print(f"Current balance for {self.acct_name}: {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry account only has a balance amount :{self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"Withdrawn {amount:.2f}. New balance: {self.balance:.2f}")
        except BalanceException as e:
            print(e)
























