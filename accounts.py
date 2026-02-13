import datetime


class Account:
    def __init__(self, name, account_id, pin, balance=0.0,
                 transaction_history=None, payees=None, active=True):
        self.name = name
        self.account_id = account_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = transaction_history if transaction_history else []
        self.payees = set(payees) if payees else set()
        self.active = active

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        if not self.active:
            return False, "Account inactive."
        if amount <= 0:
            return False, "Invalid amount."
        self.balance += amount
        self._record("DEPOSIT", amount)
        return True, "Deposit successful."

    def withdraw(self, amount):
        if not self.active:
            return False, "Account inactive."
        if amount <= 0 or amount > self.balance:
            return False, "Invalid or insufficient funds."
        self.balance -= amount
        self._record("WITHDRAW", amount)
        return True, "Withdrawal successful."

    def add_payee(self, payee_id):
        if payee_id == self.account_id:
            return False, "Cannot add yourself."
        if payee_id in self.payees:
            return False, "Payee already exists."
        self.payees.add(payee_id)
        self._record("ADD_PAYEE", 0, payee_id)
        return True, "Payee added."

    def receive_transfer(self, amount, sender_id):
        self.balance += amount
        self._record("RECEIVE", amount, sender_id)

    def send_transfer(self, amount, receiver_id):
        self.balance -= amount
        self._record("TRANSFER", amount, receiver_id)

    def deactivate(self):
        self.active = False
        self._record("ACCOUNT_CLOSED", 0)

    def _record(self, txn_type, amount, other=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append({
            "time": timestamp,
            "type": txn_type,
            "amount": amount,
            "other": other
        })

    def to_dict(self):
        return {
            "name": self.name,
            "account_id": self.account_id,
            "pin": self.pin,
            "balance": self.balance,
            "transaction_history": self.transaction_history,
            "payees": list(self.payees),
            "active": self.active
        }

    @staticmethod
    def from_dict(data):
        return Account(
            data["name"],
            data["account_id"],
            data["pin"],
            data["balance"],
            data["transaction_history"],
            data["payees"],
            data.get("active", True)
        )
