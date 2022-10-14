# This program will take an array of .ls program files, split out the relevant data of each one, and then merge them into a single .ls file
# The first part of the file where the file details are stored are taken from the first file, with the line count being updated to reflect the total number of lines in the merged file

import sys
import os
import re

# import relevant classes
from class_LSFile import LSFile


# create an array of program files
programFiles = []
# add each file in the folder ToConvert to the array
for file in os.listdir("ToConvert"):
    if file.endswith(".ls") or file.endswith(".LS"):
        programFiles.append("ToConvert/" + file)
# sort them by their filename, based on the number at the end of the file name
programFiles.sort(key=lambda x: int(re.search(r'\d+', x).group()))
print("Files to be merged:")
print(programFiles)
# create an array of program objects
programs = []
# loop through the programFiles and create a program object for each one
for programFile in programFiles:
    programs.append(LSFile(programFile))


# loop through the programs and add them to the first program
for program in programs:
    #skip first program as it is what we are adding to
    if program != programs[0]:
        programs[0].addProgram(program)

# write the merged program to a file
# remove .ls if it exists, no matter if its capital or not
fileName = programs[0].programInfo.FileName.replace(".ls", "")
fileName = fileName.replace(".LS", "")
programs[0].saveFile("Merged/" + fileName + ".LS")

print("Merged file saved to Merged/" + programs[0].programInfo.FileName)