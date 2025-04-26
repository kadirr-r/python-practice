# Ask for user input
user_input = input("Enter a number: ")

# Initialize sum
sum_of_digits = 0

# Loop through each character (digit) in the string
for digit in user_input:
    sum_of_digits += int(digit)  # Convert each character back to integer and add

# Print the result
print(f"The sum of the digits is: {sum_of_digits}")
