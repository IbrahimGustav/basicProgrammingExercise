class BankError(Exception):
    pass

class AccountAlreadyExistsError(BankError):
    pass

class NoAccountSelectedError(BankError):
    pass
