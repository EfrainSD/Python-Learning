# SAVE DATA
# Open file or if it is not created, it will
write = open("archivo.txt", "w") # With w we say we want the file in WriteMode
write.write("Hello World\nTest file\t!!!")

# IMPORTANT: Close the file
write.close()

# READ DATA
read = open("archivo.txt", "r")
# Read a line
readLine = read.readline()
print(readLine+"\n")

# IMPORTANT: Close the file
read.close()

# Read all file
read = open("archivo.txt", "r") # We can delete "r", because by default always you open it in ReadMode
readAll = read.read()
print(readAll)

# IMPORTANT: Close the file
read.close()

# We need to reopen it, because once we read a line,
# the pointer automatically points to the next one, so if we read the file after reading a line,
# it will print the entire file starting from the second line.

# Read lines
read = open("archivo.txt", "r")
readAllLines = read.readlines() # Returns a list
print(readAllLines[0])