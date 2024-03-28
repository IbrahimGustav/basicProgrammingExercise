temp = int(input("Please input the temperature: "))

if temp <= 0:
    print ("The temperature is freezing")
elif temp <= 10:
    print ("The temperature is very cold")
elif temp <= 20:
    print ("The temperature is cold")
elif temp <= 28:
    print ("The temperature is moderate")
elif temp <= 33:
    print ("The temperature is hot")
else:
    print ("The temperature is very hot") 