from bank_modules import BankAccount
from error_handling import AccountAlreadyExistsError, NoAccountSelectedError

def create_account():
    try:
        account_number = input("Enter your account number: ")
        name = input("Enter your name: ")
        nik = input("Enter your NIK: ")
        initial_balance = float(input("Enter initial balance: "))
        account = BankAccount(account_number, name, nik, initial_balance)
        print(f"Account created successfully. Account Number: {account_number}, Name: {name}, NIK: {nik}, Balance: {account.check_balance()}")
        return account
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    account = None

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("\nSelect an option: ")

        if choice == '1':
            if account:
                print("An account is already selected. Exit the program to create a new account.")
            else:
                account = create_account()
        
        elif choice == '2':
            if not account:
                print("No account selected. Please create an account first.")
            else:
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    account.deposit(amount)
                    print(f"Successfully deposited {amount}. New balance: {account.check_balance()}")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == '3':
            if not account:
                print("No account selected. Please create an account first.")
            else:
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    account.withdraw(amount)
                    print(f"Successfully withdrew {amount}. New balance: {account.check_balance()}")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == '4':
            if not account:
                print("No account selected. Please create an account first.")
            else:
                print(f"Current balance: {account.check_balance()}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()