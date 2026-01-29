import os

# Create a folder or a directory
os.makedirs("Folder")

# List content
print(os.listdir("./")) # List all things in the current directory
# You can save it in a list
foldersList = os.listdir("./")

# Show current directory
print(os.getcwd())

# Show the size of a folder
print(os.path.getsize("Folder"))

# Check if it is a folder o a directory
print(os.path.isfile("Folder"))
print(os.path.isdir("Folder"))

# Change the directory
os.chdir("Folder")
print(os.getcwd())

# Rename a folder
os.rename("Folder", "Folder_Test")

# Remove a file
os.remove(os.getcwd()+"/archivo.txt")

# Remove a folder
os.rmdir("Folder")

# IMPORTANT: If you want to enter an address directly, you must use double \\ in the url

# We can separete the name of a file from their extension using
for file in os.listdir():
    name, extension = os.path.splitext(file)
    print(name  + " " + extension)
    
# If you want to copy a file into another one
try:
    with open("archivo.txt") as file:
        with open("newArchivo.txt", "w") as newFile:
            for line in file:
                newFile.write(line)
except FileNotFoundError:
    print("File not found")