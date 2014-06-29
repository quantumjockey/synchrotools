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
	parser.add_argument("-v", "--verbose", help="Prints data to console after filtration is complete.", action="store_true")
	args = parser.parse_args()

	fileData = args.infile
	sourceFilePath = fileData.name

	filteredDataSet = RemoveEmptyLattices(fileData)
	print(fileData.name + " has been processed successfully.")
	
	if args.verbose:
		print("New dataset (raw): " + str(filteredDataSet))

	if args.separate:
		prefixedDataSet = PrefixData(filteredDataSet)
		for temp_set in IdentifyUniqueCrystals(prefixedDataSet):
			activeSet = [rawData[1] for rawData in prefixedDataSet if rawData[0] == temp_set]
			WriteDatasetToFile(activeSet, sourceFilePath, temp_set)
	else:
		WriteDatasetToFile(filteredDataSet, sourceFilePath, "")


# returns the indices for the line of data to be used as an id
def GetDataIndices(lineOfData):
	compts = lineOfData.split(",")
	return "[" + compts[0] + "," + compts[1] + "," + compts[2] + "]"


# Prefixes each line of data with a string representation of its indices
def PrefixData(dataSet):
	prefixedData = []
	for line in dataSet:
		prefixedLine = (GetDataIndices(line), line)
		prefixedData.append(prefixedLine)
	return prefixedData


# Identifies unique crystals by Miller index
def IdentifyUniqueCrystals(prefixedDataSet):
	uniqueCrystals = []
	for line in prefixedDataSet:
		if len(uniqueCrystals) == 0:
			uniqueCrystals.append(line[0])
		else:
			if line[0] not in uniqueCrystals:
				uniqueCrystals.append(line[0])
	return uniqueCrystals


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
