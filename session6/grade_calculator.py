grade = int(input("Please input your score: "))

if grade < 60 and grade >= 0:
    print ("Your grade is F")
elif grade < 70:
    print ("Your grade is D")
elif grade < 80:
    print ("Your grade is C")
elif grade < 90:
    print ("Your grade is B, congratulations!")
elif grade <= 100:
    print("Your grade is A, congratulations!")

else:
    print ("Please input a valid score")