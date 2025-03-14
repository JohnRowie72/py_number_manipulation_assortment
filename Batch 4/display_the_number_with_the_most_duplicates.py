# initialize an empty list to store the numbers
numbers = []

# start a loop to ask for input continuously
while True:

    # try to convert input to an integer
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        print("Invalid input. Stopping the program")
        break

# display the number with the most duplicates
if numbers:
    most_frequent_number = max(set(numbers), key=numbers.count)
    print(f"The number with the most duplicates is: {most_frequent_number}")

else:
    print("No numbers were entered")
