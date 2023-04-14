# A program is made up of various sections
# Program Info
# Program Lines
# Position Info

from class_P_Info import P_Info
from class_P_Lines import P_Lines
from class_P_PositionalData import P_PositionalData
import util
import os


class LSFile:
    # init is called when the class is created
    # it will take in a reference to the file name of the program to be loaded
    def __init__(self, filePath):
        # Store the file name
        self.filePath = filePath
        #get the file name from the file path
        self.fileName = os.path.basename(self.filePath)

        # Load the file
        self.loadFile()

        #if the file name is longer than 33 characters, trim it
        #dont ask me why, but the max file name length is 33 characters. if it is longer than that, the program will say the file already exists
        if len(self.fileName) > 33:
            #trim the file name to 33 characters
            self.fileName = self.fileName[:33]
            #trim leading/trailing whitespaces
            self.fileName = self.fileName.strip()
            self.filePath = os.path.dirname(self.filePath) + "/" + self.fileName
            #inform the user that the file name has been trimmed
            print("File name trimmed to 33 characters! new file name: " + self.fileName)

        #make sure the /prog name is the same as the file name
        #remove the ToConvert/ from the file name
        self.programInfo.Name = self.fileName
        self.programInfo.FileName = self.fileName

    # This function will load the file and split it into the three sections, to be passed to sub classes that will contain the data
    def loadFile(self):
        # Get the file contents
        fileContents = util.getFileContents(self.filePath)

        # Split the file into the three sections
        # the first section is up to /MN, and contains the program info itself
        # the second section is between /MN and /POS, and contains the program lines
        # the third section is after /POS to /END, and contains the position info
        programInfo = fileContents.split("/MN")[0]
        programLines = fileContents.split("/MN")[1].split("/POS")[0]
        positionInfo = fileContents.split("/POS")[1].split("/END")[0]

        # Store the program info in a ProgramInfo object
        self.programInfo = P_Info(programInfo)

        # Store the position info in a PositionInfo object
        self.positionInfo = P_PositionalData(positionInfo)

        # Store the program lines in a ProgramLines object
        self.programLines = P_Lines(programLines, self.positionInfo.getUTOOL())

    # This function will return the program string just like it was when it was read during init, but now using the stored info instead of the file
    def toString(self):
        # Create the string to be returned
        returnString = ""
        returnString += self.programInfo.toString()
        returnString += self.programLines.toString()
        returnString += self.positionInfo.toString()

        # Return the string
        return returnString

    def addProgram(self, program):
        # Get the line count of the current program
        lineCount = self.programLines.lineCount

        # update the start position number in the added program
        program.positionInfo.setStartPositionNumber(
            self.programLines.getHighestPositionalNumber() + 1)
        # Add the position info to the current program
        self.positionInfo.positions += program.positionInfo.positions

        # Set the start line number of the program to be added to the end of the current program
        program.programLines.setStartLineNumber(lineCount + 1)
        # Set the start position number of the program to be added to the end of the current program
        program.programLines.setStartPositionNumber(
            self.programLines.getHighestPositionalNumber() + 1)
        # Add the program lines to the current program
        self.programLines.lines += program.programLines.lines

        # update the line count in the program info
        self.programInfo.LineCount = self.programLines.lineCount + \
            program.programLines.lineCount

        # Return the current program
        return self

    def saveFile(self, filePath):
        util.saveFile(filePath, self.toString())
