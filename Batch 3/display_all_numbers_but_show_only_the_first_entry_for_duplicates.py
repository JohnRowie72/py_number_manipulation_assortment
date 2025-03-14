# ask the user to input 10 numbers
numbers = []
number_seen = set()

# store numbers and check for duplicates (keep only the first entry)
for i in range(10):
    number = int(input(f"Enter a number {i+1}: "))
    if number not in number_seen:
        numbers.append(number)
        number_seen.add(number)

# display the result
