import json
import random
import os
from accounts import Account


class Bank:
    def __init__(self, data_file=None):
        import os

        base_dir = os.path.dirname(os.path.abspath(__file__))
        if data_file is None:
            data_file = os.path.join(base_dir, "data", "accounts.json")

        self.data_file = data_file
        self.accounts = {}
        self._load_accounts()

    def _load_accounts(self):
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, "r") as f:
            data = json.load(f)
            for acc_id, acc_data in data.items():
                self.accounts[acc_id] = Account.from_dict(acc_data)

    def _save(self):
        with open(self.data_file, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.accounts.items()}, f, indent=4)

    def _generate_id(self):
        while True:
            acc_id = str(random.randint(10000000, 99999999))
            if acc_id not in self.accounts:
                return acc_id

    def create_account(self, name, pin, balance):
        acc_id = self._generate_id()
        acc = Account(name, acc_id, pin, balance)
        self.accounts[acc_id] = acc
        self._save()
        return acc

    def get(self, acc_id):
        return self.accounts.get(acc_id)

    def deposit(self, acc_id, amount):
        acc = self.get(acc_id)
        if not acc:
            return False, "Account not found."
        res = acc.deposit(amount)
        self._save()
        return res

    def withdraw(self, acc_id, pin, amount):
        acc = self.get(acc_id)
        if not acc or not acc.verify_pin(pin):
            return False, "Invalid credentials."
        res = acc.withdraw(amount)
        self._save()
        return res

    def add_payee(self, acc_id, payee_id):
        acc = self.get(acc_id)
        payee = self.get(payee_id)
        if not acc or not payee:
            return False, "Invalid account."
        res = acc.add_payee(payee_id)
        self._save()
        return res

    def transfer(self, sender_id, pin, receiver_id, amount):
        sender = self.get(sender_id)
        receiver = self.get(receiver_id)
        if not sender or not receiver:
            return False, "Invalid account."
        if not sender.verify_pin(pin):
            return False, "Invalid PIN."
        if receiver_id not in sender.payees:
            return False, "Payee not added."
        if amount <= 0 or sender.balance < amount:
            return False, "Invalid amount."
        sender.send_transfer(amount, receiver_id)
        receiver.receive_transfer(amount, sender_id)
        self._save()
        return True, "Transfer successful."

    def close(self, acc_id, pin):
        acc = self.get(acc_id)
        if not acc or not acc.verify_pin(pin):
            return False, "Invalid credentials."
        acc.deactivate()
        self._save()
        return True, "Account closed."
