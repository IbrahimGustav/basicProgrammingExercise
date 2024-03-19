product = []
price = []
stock = []
transaction = []
association = dict(zip(product, price, stock))

while True:
    print ("")
    print ("1. Input Products")
    print ("2. View Products")
    print ("3. Transactions")
    print ("4. Exit")
    respond_menu = int(input("Press the appropriate number to proceed: "))

    if respond_menu == 1:
        new_product = input("Please enter the product's name: ") 
        new_price = float(input("Please input the price, the final price will be calculated automatically (numbers only)"))
        new_stock = int(input("Please input the amount of stock of the product: "))
        final_price = new_price * 10/100 + new_price
        product.append (new_product)
        price.append (final_price)
        stock.append (new_stock)
        print ("Product data is registered successfully")

    elif respond_menu == 2:
        print("Product registered:")
        for i in range(len(product)):
            print(f"Product: {product[i]}, Price: {price[i]}, Stock: {stock[i]}")
            print ("")
            print ("")
    
    elif respond_menu == 3:
        print("Products available for transaction:")
        for i in range(len(product)):
            print(f"{i+1}. {product[i]}")

        selected_product_index = int(input("Enter the number of the product to perform transaction: "))
        if 1 <= selected_product_index <= len(product):
            quantity_purchased = int(input(f"How many times has '{product[selected_product_index-1]}' been purchased? "))
            if quantity_purchased <= stock[selected_product_index - 1]:
                stock[selected_product_index - 1] -= quantity_purchased
                transaction.append((product[selected_product_index - 1], quantity_purchased))
                print("Transaction successful.")
            else:
                print("Insufficient stock.")
        else:
            print("Invalid product number.")
    
    elif respond_menu == 4:
        print("Exiting program...")

    else:
        print("Invalid input. Please enter a number between 1 and 4.")