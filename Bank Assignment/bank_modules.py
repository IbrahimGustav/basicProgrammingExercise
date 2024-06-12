class BankAccount:
    def __init__(self, account_number: str, name: str, nik: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.name = name
        self.nik = nik
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self.balance -= amount

    def check_balance(self):
        return self.balance
