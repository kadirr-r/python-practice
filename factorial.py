def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x

# Ask for user input
user_input = int(input("Enter a number: "))

# Compute and display the factorial
print(f"The factorial of {user_input} is {factorial(user_input)}")
