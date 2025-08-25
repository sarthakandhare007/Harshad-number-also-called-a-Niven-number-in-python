# Harshad (Niven) Number Checker

num = int(input("Enter a number: "))

# calculate sum of digits
digit_sum = sum(int(d) for d in str(num))

# check condition
if num % digit_sum == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
