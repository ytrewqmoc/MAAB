import json
import random

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} to {self.name}'s account.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.name}'s account.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    
    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = random.randint(10000, 99999)
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)
        
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")
        return account_number  # Return the generated account number
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: ${account.balance}")
        else:
            print("Account not found.")
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, file)
    
    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {int(acc_num): Account(**details) for acc_num, details in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}


bank = Bank()
alice_account = bank.create_account("Alice", 500)
bob_account = bank.create_account("Bob", 1000)

bank.view_account(alice_account)
bank.deposit(alice_account, 200)
bank.withdraw(alice_account, 100)