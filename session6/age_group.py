age = int(input("Please input your age: "))

if age <= 12 and age >= 0:
    print ("You are a child")
elif age <= 19:
    print ("You are a teenager")
elif age <= 150:
    print ("You are an adult")
else:
    print ("Please input a valid age")