# This function will take a file name and return the file contents as a string
# Files should be read in the ToConvert folder relative to the program
def getFileContents(fileName):
    # Open the file
    file = open(fileName, "r")

    # Read the file contents
    fileContents = file.read()

    # Close the file
    file.close()

    return fileContents


# This function will take a file name and a string, and save the string to the file
# Files should be saved in the Merged folder relative to the program
def saveFile(fileName, fileContents):
    # Open the file
    file = open(fileName, "w")

    # Write the file contents
    file.write(fileContents)

    # Close the file
    file.close()
