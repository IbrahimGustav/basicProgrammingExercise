def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number = int(input("input your numbers here: "))
print(sum_of_digits(number))