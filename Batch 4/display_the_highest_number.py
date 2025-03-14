# initialize an empty list to store the numbers
numbers = []

# start a loop to take input continuously
while True:
    # try to convert input to an integer
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

        # display the highest number so far using max()
        highest_number = max(numbers)
        print(f"The highest number is: {highest_number}")

    # If input is invalid (ValueError)
    except ValueError:
        print("Invalid input. Stopping the program")
        break
