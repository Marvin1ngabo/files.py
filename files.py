# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

# File Appending
with open("my_file.txt", "a") as file:
    file.write("This is line 4\n")
    file.write("This is line 5\n")
    file.write("This is line 6\n")

# Error Handling
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
finally:
    print("File closed")
