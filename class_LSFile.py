# A program is made up of various sections
# Program Info
# Program Lines
# Position Info

from class_P_Info import P_Info
from class_P_Lines import P_Lines
from class_P_PositionalData import P_PositionalData
import util


class LSFile:
    # init is called when the class is created
    # it will take in a reference to the file name of the program to be loaded
    def __init__(self, fileName):
        # Store the file name
        self.fileName = fileName

        # Load the file
        self.loadFile()

    # This function will load the file and split it into the three sections, to be passed to sub classes that will contain the data
    def loadFile(self):
        # Get the file contents
        fileContents = util.getFileContents(self.fileName)

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

    def saveFile(self, fileName):
        util.saveFile(fileName, self.toString())
