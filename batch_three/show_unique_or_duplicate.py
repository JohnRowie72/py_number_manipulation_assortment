# create a list to store input numbers
numbers = []

# keep asking for input until an invalid entry is made
while True:
    try:
        # ask the user to input a number
        number = int(input("Enter a number: "))
        
        # check if the number is already in the list
        if number in numbers:
            print(f"{number} is now a duplicate number.")
        else:
            print(f"{number} is a unique number.")
            numbers.append(number)

    except ValueError:
        # if input is invalid, stop asking for input
        print("Invalid input. Stopping the program.")
        break
