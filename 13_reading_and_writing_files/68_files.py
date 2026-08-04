# opening a file

import os

# Option A: Relative path (file is inside a subfolder named 'data')
file_path = os.path.join("13_reading_and_writing_files", "mall_customers.csv")


# file = open(file=file_path)

# lines = file.readlines()

# for line in lines:
#     print(line)
    
    
# file.close()

# using try and finally
# try:
#     file = open(file=file_path)

#     lines = file.readlines()

#     for line in lines:
#         print(line)
        
# finally:
#     file.close()
    
    
# using the with keyword

# with open(file_path) as file:
#     lines = file.readlines()

#     for line in lines:
#         print(line)

# ----------------------------------------------------------------------

# using class

class Database():
    def __str__(self):
        return "database"
    
    def __enter__(self):
        print("Enter")
        return self
    
    
    def __exit__(self, value, type, traceback):
        print(f"{value}, {type}, {traceback}")
        print("Exit")


# with Database() as db:
#     print(db)


# ---------------------------------------------------------------------
# iterating over files

# with open(file_path) as file:
#     for line in file:
#         print(line, end="")


# -----------------------------------------------------------------------

# Writing files

import os

# Define the folder and file name
folder_name = "13_reading_and_writing_files"
file_name = "temp.txt"

# Combine into a full path
file_path = os.path.join(folder_name, file_name)

# file = open(file_path, "w")

# file.write("Hello\n")
# file.write("Bob")

# file.close()


# alternatively
# with open(file_path, 'w') as file:
#     file.write("Hello\n")
#     file.write("Bob\n")
#     file.write("How are you?")
    
# --------------------------------------------------------------------



# excersie

text = """
Apple
Banana
Milk
Egg
Onions
"""
items = list()

# with open(file_path, "w") as file:
#     file.write(text)


# with open(file_path, 'r') as file:
#     for line in file:
#         line = line.strip()
        
#         if not line:
#             continue
        
#         items.append(line)

# alternatively

# with open(file_path, 'r') as file:
#     items = [x.strip() for x in file if x.strip()]


# alternatively
# with open(file_path, 'r') as file:
#     items = list(filter(lambda y: y.strip(), map(lambda x: x.strip(), file)))


# print(items)

# ---------------------------------------------------------------------------------

# appending to files

with open(file_path, "a") as file:
    file.write("Carrot\n")











