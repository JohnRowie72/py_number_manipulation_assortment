# ask the user to input 10 numbers
numbers = []

# store the numbers in a list
for i in range(10):
    number = int(input(f"Enter a number {i+1}: "))
    numbers.append(number)
    
# check for unique numbers
# if the number appears only once, add to unique list
# display all unique numbers
