price = int(input("Please input the price in USD to know the discount: "))

if price < 50:
    print("Your final price is", price, "You received no discount")
elif price > 50 and price <= 100:
    print ("Your final price is", price - (price * 5/100), "You received 5% discount!")
elif price > 100:
    print("Your final price is", price - (price* 10/100), "You received 10% discount!")
else:
    print("Input a valid price")