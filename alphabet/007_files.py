# Read files in python

my_file = open("myfile.txt")

file_content = my_file.read()

print(file_content)

file_content = my_file.read()

print("the content is: ", file_content)

my_file.seek(0)  # Seek to the beginning of the file, at first character

file_content = my_file.read()

print("The content is : %s", file_content)
