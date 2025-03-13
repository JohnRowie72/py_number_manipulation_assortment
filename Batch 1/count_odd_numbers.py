# ask the user for 10 numbers
count_of_odd_numbers = 0

# check if each number is odd
# count how many numbers are odd
for i in range(10):
    num = float(input(f"Enter a number {i+1}: "))
    if num % 2 != 0:
        count_of_odd_numbers += 1

# print the count of odd numbers
print(f"The count of odd numbers is: {count_of_odd_numbers}")