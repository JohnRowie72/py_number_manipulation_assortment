# create a list to store input numbers
numbers = []

# keep asking for input until an invalid entry is made
while True:
    try:
        # ask the user to input a number
        number = int(input("Enter a number: "))
        
        # check if the number is already in the list
        if number in numbers:
            print(f"{number} is a duplicate.")
        else:
            print(f"{number} is unique.")
            numbers.append(number)
            
    except ValueError:
        break
