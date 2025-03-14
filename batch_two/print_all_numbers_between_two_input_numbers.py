# ask the user for two numbers
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

# determine the smaller number and the larger number
smaller_num = min(num_1, num_2)
larger_num = max(num_1, num_2)

# print all the numbers between the smaller number and the larger number
for i in range(smaller_num + 1, larger_num):
    print(i, end=" ")

print()