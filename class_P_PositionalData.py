class P_PositionalData:
    def __init__(self, positionalData):
        # Split the positional data into an array based on the ; character
        rawPositions = positionalData.split(";")

        # remove the last element of the array, as it will be empty
        rawPositions.pop()

        # each element in rawPositions is in this format
        # P[1]{
        #   GP1:
        #  UF : 0, UT : 1, CONFIG : 'N U T, 0,0,1',
        #  X = 835.896 mm,  Y = -3181.630 mm,  Z = 220.073 mm,
        #  W = 0.000 deg,  P = 75.000 deg,  R = 0.000 deg,
        #  E1 = 3175.000 mm
        #   GP2:
        #  UF : 0, UT : 1,
        #  J1 = 0.000 mm,  J2 = 0.000 mm,  J3 = 0.000 mm,
        #  J4 = 0.000 mm,  J5 = 0.000 mm,  J6 = 0.000 mm
        #   GP3:
        #  UF : 0, UT : 1,
        #  J1 = 0.000 deg
        # }
        # for the purposes of this program we can keep them in this format
        self.positions = rawPositions

        #loop through all the positions, and if E1 equals 90, set it to the value of the previous position
        for i in range(len(self.positions)):
            if "E1 = 90.000 mm" in self.positions[i]:
                self.positions[i] = self.positions[i].replace(
                    "E1 = 90.000 mm", "E1 = " + self.positions[i - 1].split("E1 = ")[1].split(" ")[0] + " mm")

        self.startPositionNumber = 1
        self.positionCount = len(self.positions)

    def toString(self):
        # Create the string to be returned
        returnString = "/POS"

        # Loop through the positions and add them to the string
        for position in self.positions:
            returnString += position + ";"

        returnString += "\n/END\n"

        # Return the string
        return returnString

    def setStartPositionNumber(self, positionNumber):
        self.startPositionNumber = positionNumber

        newPositions = []

        # loop through the positions and offset the position number
        for position in self.positions:
            originalPositionNumber = int(position.split("[")[1].split("]")[0])
            positionNumber = originalPositionNumber + self.startPositionNumber - 1
            newPosition = position.replace(
                "[" + str(originalPositionNumber) + "]", "[" + str(positionNumber) + "]")
            newPositions.append(newPosition)

        self.positions = newPositions

    def getUTOOL(self):
        # use the first position to get the UTOOL
        position = self.positions[0]

        # UTOOl is the number after UT :
        UTOOL = position.split("UT : ")[1].split(",")[0]

        return int(UTOOL)
