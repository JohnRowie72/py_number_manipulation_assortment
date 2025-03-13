# ask the user for 10 numbers
total_sum = 0

# add each number to the total sum
for i in range(10):
    num = float(input(f"Enter a number {i+1}: "))
    total_sum += num

# print the total sum
print(f"The sum of all numbers is: {total_sum}")
