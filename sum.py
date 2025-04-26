def numbers(values):
    sum_total = sum(values)
    return sum_total

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Split  user input
x = [int(i) for i in user_input.split()]

# Call the function and print the result
result = numbers(x)
print("Sum =", result)
