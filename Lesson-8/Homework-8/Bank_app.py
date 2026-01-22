import json
from abc import ABC

class Account:
    def __init__(self, account_number, name, balance: int):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'balance': self.balance
        }

    @staticmethod
    def from_dic(data):
        return Account(
            data['account_number'],
            data['name'],
            data['balance']
        )
    

accounts = []
filename = 'Bank.json'
class Bank:
    def __init__(self):
        self.accounts = []
        self.load_tasks()

    def create_account(self, account_number, name, initial_deposit: int):
        acc = Account(account_number, name, initial_deposit)
        self.accounts.append(acc)
        self.save_tasks()

    def view_account(self):
        acc_num = int(input("Enter Account number: "))
        found = False

        for account in self.accounts:
            if acc_num == account.account_number:
                print(f"{account.account_number}, {account.name}, {account.balance}")
                found = True
        if not found:
            print("Account does not exist")

    def deposit_money(self):
        acc_num = int(input("Enter the account number to deposit money: "))
        deposit = int(input("Enter the amount to deposit: "))
        updated = False
        for task in self.accounts:
            if task.account_number == acc_num:
                task.balance += deposit
                self.save_tasks()
                updated = True  
        if updated:
            print("Amount deposited successfully")
        else:
            print("Account not existent")

    def withdraw_money(self):
        acc_num = int(input("Enter the account number to withdraw money: "))
        withdrawal = int(input("Enter the amount to withdraw: "))
        updated = False
        for account in self.accounts:
            if account.account_number == acc_num:
                if account.balance >= withdrawal:
                    account.balance -= withdrawal
                    self.save_tasks()
                    updated = True
                if account.balance < withdrawal:
                    print("Insufficient balance") 
                    return 
        if updated:
            print("Amount withdrawn successfully")
        else:
            print("Account not existent")

    def save_tasks(self):
        with open(filename, 'w') as file:
            json.dump([account.to_dict() for account in self.accounts], file)
        
    def load_tasks(self):
        try:
            with open(filename, 'r') as file:
                self.accounts = [Account.from_dic(data) for data in json.load(file)]
        except FileNotFoundError:
            self.accounts = []

if __name__ == "__main__":
    app = Bank()
    #app.create_account(101, "john", 100)
    #app.view_account()
    #app.deposit_money()
    app.withdraw_money()


    

        



