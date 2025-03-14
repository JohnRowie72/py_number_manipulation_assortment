# initialize an empty list to store the numbers
numbers = []

# start a loop to take input continuously
while True:
    # try to convert input to an integer
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)
        
        # sort the list in descending
        # display the sorted list
    # if input is invalid (ValueError)
        # print error message
        # break the loop
