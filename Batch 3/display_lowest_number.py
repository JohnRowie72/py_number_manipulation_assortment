# create a list to store inputs
numbers = []

# keep askibf for input until an invalid entry is made
while True:
    try:
        # ask the user to input a number
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        # if input is invalid, stop asking for input
        print("Invalid input. Stopping the program.")
        break

# display the lowest number
if numbers:
    print(f"The lowest number entered is: {min(numbers)}")

else:
    print("No numbers were entered")
