a = int(input("Please input value A: "))
b = int(input("Please input value B: "))
menu = int(input("Which operation do you want to do? 1. Addition 2. Subtraction 3. Multiplication 4. Division "))

if menu == 1:
    print ("The addition of", a, "and", b, "is", a + b)
elif menu == 2:
    print ("The substraction of", a, "and", b, "is", a - b)
elif menu == 3:
    print ("The multiplication of", a, "and", b, "is", a * b)
elif menu == 4:
    print ("The division of", a, "and", b, "is", a/b)
else:
    print ("Please input the correct menu item")