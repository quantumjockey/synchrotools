# Description: Allows user to separate data from a synchrotron output file by phase via the terminal.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import argparse
import os
import sys
from collections import deque
from copy import deepcopy
from dataFormatting import FormatData
from pathops import CreateDirectory
from pathops import Newline

# script body for file processing
def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin, help='File to be parsed.')
	parser.add_argument("-d", "--dat", help="Process as .dat file (outputs .txt for parsed files by default.", action="store_true")
	parser.add_argument("-x", "--x_y", help="Process as .x_y file (outputs .txt for parsed files by default.", action="store_true")
	args = parser.parse_args()

	fileData = args.infile
	sourceFile = fileData.name

	if args.dat:
		processingExtension = ".dat"
	elif args.x_y:
		processingExtension = ".x_y"
	else:
		processingExtension = ".txt"

	head = os.path.split(sourceFile)[0]
	tail = os.path.split(sourceFile)[1]

	if head != "":
		head += "/"

	directory = head + "ParsedData_" + tail + "(" + processingExtension + ")";

	CreateDirectory(directory)
	ProcessTextFile(fileData, directory, processingExtension)


# Generate a file name and path for the current set of data
def GetFileNameAndPath(directory, xValue, yValue, extension):
	parsedFileName = "Sample_" + xValue + "x" + yValue + "y" + extension
	parsedFilePath = directory + "/" + parsedFileName
	return parsedFilePath


# Parse the text file data
def ProcessTextFile(sourceFile, targetFileDirectory, extension):
	lineOfData = []
	sampleData = []
	xVal = ""
	yVal = ""
	numLines = 0
	numPaths = 0
	path = ""
	phaseData = deque()

	for line in sourceFile:
		lineOfData = line.split()

		if xVal != lineOfData[0] and xVal != "" or yVal != lineOfData[1] and yVal != "":
			WriteDataToFile(targetFileDirectory, xVal, yVal, extension, phaseData)
			numPaths += 1

		xVal = lineOfData[0]
		yVal = lineOfData[1]

		sampleData = [lineOfData[2], lineOfData[3]]
		phaseData.append(deepcopy(sampleData))
		numLines += 1

	WriteDataToFile(targetFileDirectory, xVal, yVal, extension, phaseData)
	numPaths += 1

	print("Processed " + str(numLines) + " data points.")
	print("Resolved " + str(numPaths) + " phases.")


# Writes queue containing phase data to file
def WriteDataToFile(targetFileDirectory, xVal, yVal, extension, phaseData):
	colWidth = 10
	path = GetFileNameAndPath(targetFileDirectory, xVal, yVal, extension)
	print("Writing to " + path)
	fout = open(path, 'w')
	while len(phaseData) != 0:
		data = phaseData.popleft()
		fout.write(FormatData(colWidth, str(data[0])) + FormatData(colWidth, str(data[1])) + Newline())
	fout.close()


# Call main function
if __name__ == "__main__":
	main()
