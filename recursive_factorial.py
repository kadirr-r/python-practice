def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Ask for user input
user_input = int(input("Enter a number: "))

# Compute and display the factorial
print(f"The factorial of {user_input} is {factorial(user_input)}")
