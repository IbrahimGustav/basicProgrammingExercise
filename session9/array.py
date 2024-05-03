product_list = []

print("""Menu:
1. View products
2. Add a product
3. Delete a product
4. Delete a product based on the product number
5. Exit""")

while True:
    menu = input("To navigate, please input the number for the menu you want to choose: ")
    
    if menu == '1':
        print("Products:", product_list)
        
    elif menu == '2':
        product = input("Input the product name: ")
        product_list.append(product)
        print("Product added! Products: ", product_list)
        
    elif menu == '3':
        product = input("Please type the item you wish to delete: ")
        if product in product_list:
            product_list.remove(product)
            print("Product deleted successfully!")
        else:
            print("Invalid item, make sure you type the product correctly")
            
    elif menu == '4':
        index = input("Enter index to delete: ")
        try:
            index = int(index)
            if 0 <= index < len(product_list):
                del product_list[index]
                print("Product deleted successfully!")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid index!")
            
    elif menu == "5":
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice!")
