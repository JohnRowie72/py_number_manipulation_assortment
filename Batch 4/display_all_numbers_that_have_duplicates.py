# initialize an empty list to store the numbers
numbers = [] 

# ask the user for 10 numbers and store them in the list
for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

# initialize an empty list to store duplicate numbers
duplicates = []

# loop through the list
for number in numbers:

    # if a number appears more than once and is not yet in the duplicates list
    if numbers.count(number) > 1 and number not in duplicates:

        # add it to the duplicates list
        duplicates.append(number)

# display the duplicate numbers
if duplicates:
    print(f"The duplicate numbers are: {duplicates}")
else:
    print("No duplicate numbers found")

