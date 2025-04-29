# open()

file = open("Assets/asset.txt", "r") 
mode = file.read()

print(mode)  # Print the content of the file

# * Example the "w"

file = open("Assets/asset.txt", "w")  # Opens file in write mode
file.write("Hello, Python Learners!")
file.close() # Close the file after writing

