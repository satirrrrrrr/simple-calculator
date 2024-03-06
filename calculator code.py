# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display calculation history
def display_history(history):
    if history:
        print("Calculation History:")
        for entry in history:
            print(entry)
    else:
        print("Calculation History is empty.")

# Main function to run the my simple calculator
def main():
    history = []  # Empty list to store calculation history
    while True:
        print("\nWelcome to Simple Calculator App")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '6':
            print("Thank you for using my simple calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = f"(num1) + (num2) = (result)"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"(num1) - (num2) = (result)"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"(num1) * (num2) = (result)"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"(num1) / (num2) = (result)"

            print("Result:", result)
            history.append(operation)

        elif choice == '5':
            display_history(history)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()