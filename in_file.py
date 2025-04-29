#* Recap of File Handling in Python
#* 1. File handling is the process of creating, reading, writing, and manipulating files in Python.


#? Reading the whole file
#! The `read()` method reads the entire content of the file and returns it as a string.

with open("assets/in_file.txt", "r") as input_file:
 file_contents = input_file.read()
 print(file_contents)  # Print the content of the file


# 1. The `with` statement is used to open the file, ensuring it is properly closed after use.
# 2. The file is opened in read mode ("r"), allowing you to read its contents.
# 3. The `read()` method reads the entire content of the file and stores it in the variable `file_content`.
# 4. Finally, the content is printed to the console.

    
#? When do we use the `with` statement?

"""

The `with` statement is used to ensure that the file is properly
closed after its block of code is executed, 
even if an error occurs. This helps prevent 
resource leaks and ensures that file handles are released correctly.
It is a best practice to use the `with` statement when working 
with files in Python, as it simplifies file handling 
makes the code cleaner and more readable.

"""
    

"""

The `with` statement automatically takes care of closing the file for you, 
so you don't have to explicitly call `file.close()`.
This is especially important in larger programs where 
forgetting to close a file can lead to resource leaks and other issues.

"""

"""

The `open()` function is used to open a file, specifying 
the file name and mode (e.g., "r" for read, "w" for write, "a" for append).
The `read()` method reads the entire content of the file, 
while `readline()` reads a single line, and `readlines()` reads all lines into a list.
The `write()` method is used to write data to a file, 
and `writelines()` can write multiple lines at once.
Always close the file after performing operations to free up system resources. 
This can be done using the `close()` method or by using the `with` statement,
which automatically closes the file when done.

"""




#? What does as input_file mean?


"""
The `as input_file` part of the `with open("assets/in_file.txt", "r") as input_file:` statement 
assigns the opened file object to the variable `input_file`. 
This allows you to refer to the file object using the variable 
name `input_file` within the block of code that follows. 
It is a common practice to use descriptive variable names for better code readability.

"""


#! Reading a line from the file using the 'readline()' method
with open("assets/in_file.txt", "r") as input_file:
  first_line = input_file.readline()  # Read the first line of the file

  print(first_line)  # Print the first line to the console - Output: First line
  

#? Read all lines into a using bracket notation

with open("assets/in_file.txt", "r") as input_file:
  lines = input_file.readlines()  
second_line = lines[1]  # Second line (index 1)
third_line = lines[2]  # Third line (index 2)
fourth_line = lines[3]  # Fourth line (index 3)
fifth_line = lines[4]  # Fifth line (index 4)
# .strip() removes the extra '\n' at the end of the line
# .strip() removes leading and trailing whitespace characters (including newlines) from the string.

print(second_line) 
print(third_line)  # Print the second and third lines to the console - Output: Second line, Third line
print(fourth_line)  # Print the fourth line to the console - Output: Fourth line
print(fifth_line)  # Print the fifth line to the console - Output: Fifth line



# ? Reading a number of characters from the file
with open("assets/in_file.txt", "r") as input_file:
 first_five_letters = input_file.read(5)
 print(first_five_letters)  # Print the first five characters of the file - Output: First