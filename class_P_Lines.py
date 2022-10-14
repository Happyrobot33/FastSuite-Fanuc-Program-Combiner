from class_P_Instruction import P_Instruction


class P_Lines:
    # init takes in a string of the program lines
    def __init__(self, programLines, UTOOL):
        # Split the program lines into an array based on the ; character
        rawLines = programLines.split(";")

        # remove the last element of the array, as it will be empty
        rawLines.pop()

        # loop through the lines and convert them into P_Instruction objects
        self.lines = []
        for line in rawLines:
            #check to make sure the instruction isnt any of these first
            # UTOOL_NUM
            # UFRAME_NUM
            if not "UTOOL_NUM" in line and not "UFRAME_NUM" in line:
                self.lines.append(P_Instruction(line))

        # add in comments to the start and end of the line array to indicate a seperate program
        self.lines.insert(0, P_Instruction(
            "NULL: CALL PICK_TOOL_" + str(UTOOL)))
        self.lines.insert(0, P_Instruction("NULL: !Start of merged program"))
        self.lines.insert(0, P_Instruction("NULL: "))
        self.lines.append(P_Instruction("NULL: !End of merged program"))
        self.lines.append(P_Instruction("NULL: "))

        self.startLineNumber = 1
        self.lineCount = len(self.lines)

    # This function will return the program lines as a string
    def toString(self):
        # Create the string to be returned
        returnString = "/MN\n"

        # Loop through the lines and add them to the string
        lineNumber = self.startLineNumber
        for line in self.lines:
            # calculate the correct number of spaces to add to the line number to keep the formatting correct
            spaces = " " * (4 - len(str(lineNumber)))
            returnString += spaces + \
                str(lineNumber) + ":" + line.toString() + ";\n"
            lineNumber += 1

        # Return the string
        return returnString

    def setStartLineNumber(self, lineNumber):
        self.startLineNumber = lineNumber

    def setStartPositionNumber(self, positionNumber):
        for line in self.lines:
            line.offsetPointNumber(positionNumber - 1)

    def getHighestPositionalNumber(self):
        highestPositionalNumber = 0
        for line in self.lines:
            if line.getPointNumber() > highestPositionalNumber:
                highestPositionalNumber = line.getPointNumber()
        return highestPositionalNumber
