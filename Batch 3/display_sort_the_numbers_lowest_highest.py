# initialize an empty list to store the numbers
numbers = []

# start a loop to take user input continuously
while True:
    try:
        # try to convert input to an integer
        number = int(input("Enter a number: "))

        # add the number to the list
        numbers.append(number)

        # sort the list in ascending order
        numbers.sort()
        
        # display the sorted list
    # if input is invalid (ValueError)
        # print error message
        # break the loop
