# initialize an empty list to store the numbers
numbers = []

# start a loop to take user input continuously
while True:
    try:
        # try to convert input to an integer
        number = int(input("Enter a number: "))
        # add the number to the list
        numbers.append(number)

    except ValueError:
        print("Invalid input. Stopping the program")
        break

# display and to sort the list in ascending order
if numbers:
    numbers.sort()
    # display the sorted list
    print(f"The numbers from lowest to highest: {numbers}")

else:
    print("No numbers were entered")
