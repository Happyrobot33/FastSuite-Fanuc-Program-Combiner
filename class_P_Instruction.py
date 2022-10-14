# This class stores information about the instruction in each line
class P_Instruction:
    def __init__(self, line):
        # coming in is a string of the line, it may actually be multiple lines depending on how long the instruction is

        # Examples of instructions:
        #   1:  UFRAME_NUM = 0;
        #   2:  UTOOL_NUM = 1;
        #   3:J P[1] 50% FINE;
        #   4:J P[2] 50% FINE;
        #   5:J P[3] 50% FINE;
        #   6:L P[4] 1000mm/sec FINE
        #    :  SPOT[SD=1,P=1,t=1.0,S=2,ED=1] ;

        # get the instruction after the first : character
        # make sure everything after is still kept, even if there is another : character
        splitInstruction = line.split(":")
        self.instruction = splitInstruction[1:len(splitInstruction)]

        # make the instruction a string, adding back in the : character between each part
        self.instruction = ":".join(self.instruction)

        # if the instruction is instruction with a point number, then store the point number
        if "P[" in self.instruction:
            # get the point number
            pointNumber = self.instruction.split("P[")[1].split("]")[0]

            # store the point number
            self.pointNumber = int(pointNumber)

            # remove the point number from the instruction
            self.instruction = self.instruction.replace(
                "P[" + pointNumber + "]", "P[]")

    # This function will return the instruction as a string
    def toString(self):
        # Create the string to be returned
        returnString = self.instruction

        # if the instruction is an instruction with a point number, then add the point number back in
        if hasattr(self, "pointNumber"):
            returnString = returnString.replace(
                "P[]", "P[" + str(self.pointNumber) + "]")

        # Return the string
        return returnString

    def offsetPointNumber(self, offset):
        # if the instruction is an instruction with a point number, then add the offset to the point number
        if hasattr(self, "pointNumber"):
            self.pointNumber += offset

    def getPointNumber(self):
        # if the instruction is an instruction with a point number, then return the point number
        if hasattr(self, "pointNumber"):
            return self.pointNumber
        else:
            return 0
