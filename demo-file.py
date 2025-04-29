
# What is file handling in Python?
# File handling in Python refers to the process of creating, reading, writing, and manipulating files on a computer system using Python programming language.

# It allows developers to interact with files, such as text files, binary files, and more, enabling them to store and retrieve data efficiently.

# File handling is essential for tasks like data storage, configuration management, and logging.

# Python provides built-in functions and libraries to perform file operations, making it easy to work with files.

# File handling in Python is done using built-in functions and methods provided by the language. The most common operations include:

# *Examples

#? 1. Opening a file: You can open a file using the `open()` function, which takes the file name and mode (read, write, append, etc.) as arguments.

file = open("file.txt", "r")  # Open a file in read mode

#? 2. Reading from a file: You can read the contents of a file using methods like `read()`, `readline()`, or `readlines()`.
content = file.read()  # Read the entire file content

print(content)  # Print the content of the file



#* Example
# ? 3. Writing to a file: You can write data to a file using the `write()` or `writelines()` methods. Be cautious, as writing will overwrite existing content unless you open the file in append mode.
# ? 4. Closing a file: After performing file operations, it's important to close the file using the `close()` method to free up system resources.
file = open("file.txt", "w")  # Opens file in write mode
file.write("Hello, Python Learners!")
file.close() # Close the file after writing 


# Module 3: Writing to Files

# Writing with write() and writelines()

# Difference between write mode (w) and append mode (a)

# Creating new files
with open("new_file.txt", "w") as f:
    f.write("This is a new file created in write mode.")
    
with open("new_file.txt", "w") as f:
    f.write("This will overwrite existing content.")

with open("new_file.txt", "a") as f:
    f.write("\nThis will be added at the end.")
    
    # why is this not working?
with open("new_file.txt", "a") as f:
    f.write("\nThis will be added at the end.")


# Reading the file to check the content

# Append mode (a) allows you to add content to the end of the file without overwriting existing data. This is useful for logging or appending new information.

with open("new_file.txt", "r") as f:
    content = f.read()
    print(content)  # Print the content of the file to verify the changes
    
    
    


