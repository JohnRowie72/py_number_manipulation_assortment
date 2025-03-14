# initialize an empty list to store the numbers
numbers = []

# start a loop to take input continuously
while True:
    # try to convert input to an integer
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        print("Invalid input. Stopping the program")
        break

# display the numbers from highest to lowest
if numbers:
    # sort the list in descending
    numbers.sort(reverse=True)

    # display the sorted list
    print(f"The numbers from highest to lowest: {numbers}")

else:
    print("No numbers were entered.")
