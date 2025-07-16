# Create a program that:

# Prompts the user to enter a message.

# Appends that message to a text file (e.g., log.txt).

# Then reads and displays the full content of the file.

def write_log(message, fileName="log.txt"):
    with open(fileName, "a") as file:
        file.write(message + "\n")

def read_log(fileName="log.txt"):
    with open(fileName, "r") as file:
        content = file.read()

message = input("Enter a message to log: ")
write_log(message)

print("\nCurrent log content: ")
print(read_log())
