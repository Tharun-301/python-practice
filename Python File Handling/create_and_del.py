import os
# # Two ways to create a new file

# # Opens a file for writing, creates the file if it does not exist
# f = open("name_list.txt", "w")
# f.close()

# # Creates the specified file, but returns an error if the file exists
# if not os.path.exists("indexfile.txt"):
#     f = open("dave.txt", "x")
#     f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("name_list.txt"):
    os.remove("name_list.txt")
else:
    print("The file you wish to delete does not exist")


