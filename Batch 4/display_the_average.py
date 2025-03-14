# initialize an empty list to store the numbers
numbers = []

# start a loop to take input continuously
while True:
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        print("Invalid input. Stopping the program")
        break
    
# display the result
