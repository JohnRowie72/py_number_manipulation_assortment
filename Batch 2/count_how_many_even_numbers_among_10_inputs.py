# ask the user to input 10 numbers
count_even = 0

# check if each number is even
# count how many numbers are even
for i in range(10):
    number = int(input(f"Enter a number {i+1}: "))
    if number % 2 == 0:
        count_even += 1

# print the count of even numbers
print(f"The count of even numbers is {count_even}")
