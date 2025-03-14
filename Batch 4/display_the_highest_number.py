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

# display the highest number so far using max()
if numbers:
    highest_number = max(numbers)
    print(f"The highest number is: {highest_number}")

else:
    print("No numbers were entered.")
