# print all number 0 - 100

for number in range(0, 101):
   
    # check if ending with 0 or 5
    if number % 10 != 0 and number % 10 != 5:

        # print if true
        print(number, end=" ")

print()
