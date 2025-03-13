# ask user for two numbers
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

# if the second number is not zero, compute the quotient of the two numbers then print the result with a decimal point
# if the second number is zero, print an error message
if num_2 != 0:
    quotient_of_two_numbers = num_1 / num_2
    print("The quotient of the two numbers is:", quotient_of_two_numbers)
else:
    print("Error: Cannot divide by zero")