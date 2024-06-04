import calculator_functions

def calculator():
    print("Select the desired operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    
    choice = input("Please choose the appropriate number (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    calculator()
