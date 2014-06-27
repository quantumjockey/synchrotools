# Description: Allows user to purge mis-measurements from crystal lattice data.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import argparse
import os
import sys
from pathops import Newline

# script body for file processing
def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin, help='File to be parsed.')
	args = parser.parse_args()

	fileData = args.infile
	sourceFilePath = fileData.name

	dataSet = RemoveEmptyLattices(fileData)
	print(fileData.name + " has been processed successfully.")
	print("New dataset (raw): " + str(dataSet))
	WriteDatasetToFile(dataSet, sourceFilePath)


# Removes empty [0,0,0] [h,k,l] lattices from the dataset
def RemoveEmptyLattices(fileData):
	data = []
	filteredData = []
	targetPath = ""
	lineIndex = 0

	for line in fileData:
		if lineIndex > 1:
			lineOfData = line.replace(" ","").strip("\r\n")
			data = lineOfData.split(',')
			numZeroes = 0;
			i = 0;
			for dataPoint in data:
				if i < 3 and dataPoint == "0":
					numZeroes += 1
				i += 1
			if numZeroes < 3:
				filteredData.append(lineOfData)
		lineIndex += 1
	return filteredData


# Writes a dataset to file
def WriteDatasetToFile(data, path):
	path = GetFileNameAndPath(path)
	print("Writing to " + path)
	fout = open(path, 'w')
	for row in data:
		fout.write(row + Newline())
	fout.close()
	print("Dataset has been successfully written to " + path)


# Generate a file name and path for the current set of data
def GetFileNameAndPath(sourcePath):
	head = os.path.split(sourcePath)[0]
	tail = os.path.split(sourcePath)[1]
	if head != "":
		head += "/"
	return head + "Filtered_set_" + tail


# Call main function
if __name__ == "__main__":
	main()
