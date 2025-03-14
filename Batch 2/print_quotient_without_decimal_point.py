# ask the user for two numbers
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

# if the second number is not zero, compute the integer division
# print the quotient without the decimal point
if num_2 != 0:
    print(f"The quotient of {num_1} and {num_2} without decimal is {num_1 // num_2}")

# if the second number is zero, print an error message
else:
    print("Error: Division by zero is not allowed.")
