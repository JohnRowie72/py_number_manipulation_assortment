# create a list to store inputs
numbers = []

# keep askibf for input until an invalid entry is made
while True:
    try:
        # ask the user to input a number
        number = int(input("Enter a number: "))
        numbers.append(number)
        
        # display the result
        print(f"The lowest number entered is: {min(numbers)}")

    except ValueError:
        # if input is invalid, stop asking for input
        print("Invalid input. Stopping the program.")

