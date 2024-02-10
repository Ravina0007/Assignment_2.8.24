numbers = []

while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    numbers.append(int(number))

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Print the five greatest numbers
print("Five greatest numbers (in descending order):", numbers[:5])
