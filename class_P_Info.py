class P_Info:
    #init takes in a string of the program info
    def __init__(self, programInfo):
        #Split the program info into the relevant variables
        #The first line is the program name after /PROG 
        self.Name = programInfo.split("/PROG ")[1].split("\n")[0]

        self.Owner =            programInfo.split("OWNER")[1].split("= ")[1].split(";")[0]
        self.Comment =          programInfo.split("COMMENT")[1].split("= ")[1].split(";")[0]
        self.Size =             programInfo.split("PROG_SIZE")[1].split("= ")[1].split(";")[0]
        self.CreateDate =       programInfo.split("CREATE")[1].split("= ")[1].split(";")[0]
        self.ModifyDate =       programInfo.split("MODIFIED")[1].split("= ")[1].split(";")[0]
        self.FileName =         programInfo.split("FILE_NAME")[1].split("= ")[1].split(";")[0]
        self.Version =          programInfo.split("VERSION")[1].split("= ")[1].split(";")[0]
        self.LineCount =        programInfo.split("LINE_COUNT")[1].split("= ")[1].split(";")[0]
        self.MemorySize =       programInfo.split("MEMORY_SIZE")[1].split("= ")[1].split(";")[0]
        self.Protect =          programInfo.split("PROTECT")[1].split("= ")[1].split(";")[0]

        #sanitize create date and modify date to remove AM or PM
        self.CreateDate = self.CreateDate.replace("AM", "")
        self.CreateDate = self.CreateDate.replace("PM", "")
        self.ModifyDate = self.ModifyDate.replace("AM", "")
        self.ModifyDate = self.ModifyDate.replace("PM", "")

        #TCD is complicated as it is a list of values, each on a new line delimited by a comma
        #Example is:
        #TCD: STACK_SIZE      = 0,
        #     TASK_PRIORITY   = 50,
        #     TIME_SLICE      = 0,
        #     BUSY_LAMP_OFF   = 0,
        #     ABORT_REQUEST   = 0,
        #     PAUSE_REQUEST   = 0;
        #So we need to get the lines between TCD: and ;
        #Then split each line on the = and ,
        #Then strip the whitespace from the start and end of each value
        #Then store the values in a dictionary
        self.TCDLines = programInfo.split("TCD:")[1].split(";")[0].split("       = ")

        self.DefaultGroup =     programInfo.split("DEFAULT_GROUP")[1].split("= ")[1].split(";")[0]
        self.ControlCode =      programInfo.split("CONTROL_CODE")[1].split("= ")[1].split(";")[0]

    #This function will return the program info as a string
    def toString(self):
        compiledString = ""
        #Start with the program name
        compiledString += "/PROG " + self.Name + "\n"
        compiledString += "/ATTR\n"
        compiledString += "OWNER           = " + self.Owner + ";\n"
        compiledString += "COMMENT         = " + self.Comment + ";\n"
        compiledString += "PROG_SIZE       = " + self.Size + ";\n"
        compiledString += "CREATE          = " + self.CreateDate + ";\n"
        compiledString += "MODIFIED        = " + self.ModifyDate + ";\n"
        compiledString += "FILE_NAME       = " + self.FileName + ";\n"
        compiledString += "VERSION         = " + self.Version + ";\n"
        compiledString += "LINE_COUNT      = " + str(self.LineCount) + ";\n"
        compiledString += "MEMORY_SIZE     = " + self.MemorySize + ";\n"
        compiledString += "PROTECT         = " + self.Protect + ";\n"

        #TCD is a bit more complicated, as it is a list of values in a specific format
        #TCD: STACK_SIZE      = 0,
        #     TASK_PRIORITY   = 50,
        #     TIME_SLICE      = 0,
        #     BUSY_LAMP_OFF   = 0,
        #     ABORT_REQUEST   = 0,
        #     PAUSE_REQUEST   = 0;
        compiledString += "TCD:" + self.TCDLines[0] 
        for i in range(1, len(self.TCDLines)):
            compiledString += self.TCDLines[i]
        compiledString += ";\n"

        compiledString += "DEFAULT_GROUP   = " + self.DefaultGroup + ";\n"
        compiledString += "CONTROL_CODE    = " + self.ControlCode + ";\n"
        compiledString += "/APPL\n"
        compiledString += "  SPOT : TRUE ;\n"
        compiledString += "  SPOT Welding Equipment Number : 1 ;\n"

        return compiledString