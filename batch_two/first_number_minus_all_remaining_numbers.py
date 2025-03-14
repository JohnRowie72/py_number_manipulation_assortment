# ask the user for 10 numbers
num_1 = float(input("Enter the first number: "))
sum_result = num_1

# subtract the remaining 9 numbers from the first number
for i in range(9):
    number = float(input("Enter the next number: "))
    sum_result -= number

# print the result
print(f"The result of subtracting all the numbers from the first number is {sum_result}")
