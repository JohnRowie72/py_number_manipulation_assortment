# initialize an empty list to store the numbers
numbers = []

# start a loop to take input continuously
while True:
    # try to convert input to an integer
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

        # sort the list in descending
        numbers.sort(reverse=True)

        # display the sorted list
        print(f"The numbers from highest to lowest: {numbers}")

    # if input is invalid (ValueError)
    except ValueError:
        # print error message
        print("Invalid input. Stopping the program")
        break
