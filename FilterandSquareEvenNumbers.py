# Write a program that:

# Takes a list of integers from the user (input separated by spaces).

# Filters out the even numbers.

# Creates a new list with the squares of those even numbers.

# Prints the resulting list.

def get_numbers():
    raw_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, raw_input.split()))
    return numbers

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

def main():
    numbers = get_numbers()
    even_numbers = filter_even_numbers(numbers)
    squared_even_numbers = square_numbers(even_numbers)
    
    print("Even numbers:", even_numbers)
    print("Squared even numbers:", squared_even_numbers)

if __name__ == "__main__":
    main()
