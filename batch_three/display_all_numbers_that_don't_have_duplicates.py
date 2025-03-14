# ask the user to input 10 numbers
numbers = []
unique_numbers = []

# store the numbers in a list
for i in range(10):
    number = int(input(f"Enter a number {i+1}: "))
    numbers.append(number)

# check for unique numbers
# if the number appears only once, add to unique list
for number in numbers:
    if numbers.count(number) == 1:
        unique_numbers.append(number)

# display all unique numbers
if unique_numbers:
    print(f"The unique numbers are: {unique_numbers}")

else:
    print("There are no unique numbers.")
    