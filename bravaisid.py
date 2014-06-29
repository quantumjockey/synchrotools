# Description: Allows user to purge mis-measurements from crystal lattice data.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import argparse
import os
import sys
from collections import deque
from copy import deepcopy
from pathops import Newline

# script body for file processing
def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin, help='File to be parsed.')
	parser.add_argument("-s", "--separate", help="Separates crystal data by Miller index.", action="store_true")
	args = parser.parse_args()

	fileData = args.infile
	sourceFilePath = fileData.name

	filteredDataSet = RemoveEmptyLattices(fileData)
	print(fileData.name + " has been processed successfully.")
	print("New dataset (raw): " + str(filteredDataSet))

	if args.separate:
		# for _set in IdentifyUniqueCrystals(filteredDataSet):
		# 	for line in _set:
		# 		print(GetDataIndices(line))
		# WriteDatasetToFile(_set, sourceFilePath, set_id)
	else:
		WriteDatasetToFile(filteredDataSet, sourceFilePath, "")


# returns the indices for the line of data to be used as an id
def GetDataIndices(lineOfData):
	compts = lineOfData.split(",")
	return "[" + compts[0] + "," + compts[1] + "," + compts[2] + "]"


# Identifies unique crystals by Miller index
def IdentifyUniqueCrystals(dataSet):
	uniqueSets = []
	i = 0
	for line in dataSet:
		if i == 0:
			parsed = (GetDataIndices(line), [line])
			uniqueSets.append(parsed)
		else:
			for identifier in [_set[0] for _set in uniqueSets]:
				indices = GetDataIndices(line)
				if identifier == indices:
					
				else:
					parsed = (GetDataIndices(line), [line])
					uniqueSets.append(parsed)
		i += 1
	uniqueSets.append(dataSet)
	return uniqueSets


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
def WriteDatasetToFile(data, path, set_id):
	path = GetFileNameAndPath(path, set_id)
	print("Writing to " + path)
	fout = open(path, 'w')
	for row in data:
		fout.write(row + Newline())
	fout.close()
	print("Dataset has been successfully written to " + path)


# Generate a file name and path for the current set of data
def GetFileNameAndPath(sourcePath, set_id):
	head = os.path.split(sourcePath)[0]
	tail = os.path.split(sourcePath)[1]
	if head != "":
		head += "/"
	if set_id == "":
		return head + "Filtered_set_" + tail
	else:
		return head + "Filtered_set_" + set_id + "_" + tail	


# Call main function
if __name__ == "__main__":
	main()
