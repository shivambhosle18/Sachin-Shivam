# with open("databse.txt") as f - works same as 2nd and last line i.e. f.close()
f = open("database.txt", "rt")

print(f.readline())  # reads line by line
print(f.readlines())  #read lines till the end
print(f.tell())  # Tells us where is the pointer

f.seek(0)  #pointer goes to the character entered in bracket 
x = f.read()
print(x)

# f = open("database.txt", "rt") - read mode default
# f = open("database.txt", "r+") - read and write both 
# f = open("database.txt", "w") - over write file / create new file and write
# f = open("database.txt", "r") -  read only 
# f = open("database.txt", "rb") - read binary 
# f = open("database.txt", "a") - append Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist


f.close()



# This method is not entirely safe. 
# If an exception occurs when we are performing some operation with the file, 
# the code exits without closing the file.

try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()