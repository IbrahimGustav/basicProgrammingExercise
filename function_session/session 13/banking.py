def createaccount():
    accounts_list =[]
    account_name = input("Please input your legal name: ")
    account_address = input("Please input your address")
    account_age = input("Please input your age: ")
    account = [account_name, account_address, account_age]
    accounts_list.append(account)

def deposit()