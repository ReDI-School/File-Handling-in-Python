
#? Writing into a file

#* with open("assets/out_file.txt", "w") as output_file:

#* What does "w" mean?
# The "w" mode in the `open()` function stands for "write."


"""
The "w" mode is used to write data to a file.
This mode is typically used when you want to create a new file 
or overwrite an existing file with new data.
If you want to append data to an existing file 
without truncating it, you can use the "a" mode (append) instead.

"""

# Use Case 1: Writing a single line to a file
with open("assets/out_file.txt", "w") as output_file:
    output_file.write("This is a new session again.\n")  # Write a single line to the file
# The "\n" at the end adds a newline character to separate lines in the file.



"""
The `writelines()` method takes a list of strings and writes them to 
the file without adding newline characters automatically.
You need to include the newline characters in the strings
if you want them to appear on separate lines in the file.

"""

with open("assets/out_file.txt", "w") as output_file:
    lines_to_write = [
        "This is the first line.\n",
        "This is the second line.\n",
        "This is the third line.\n"
    ]
    output_file.writelines(lines_to_write)  # Write multiple lines to the file
# Example 2: Writing multiple lines to a file

    

#? Example 3: Appending to a file


with open("assets/out_file.txt", "a") as output_file:
    output_file.write("This line will be appended to the file.\n")  # Append a line to the file
  


"""
The "a" mode is used to open the file for appending, 
which means new content will be 
added to the end of the file without truncating it.
This is useful when you want to add new data to an 
existing file without losing the previous content.

"""  

# Use append "a" mode to append4 lines the file
with open("assets/out_file.txt", "a") as output_file:
    lines_to_append = [
        "This is the first appended line.\n",
        "This is the second appended line.\n",
        "This is the third appended line.\n"
        "0: Project Time : 28th April 2025\n",
        "1: Student Ipek ID: 353637474\n",
        "1: Student Udua ID: 353637474\n",
        "2: Student Chima ID: 353637474\n",
    ]
    output_file.writelines(lines_to_append)  # Append multiple lines to the file
