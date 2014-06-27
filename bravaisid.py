# Description: Allows user to purge mis-measurements from crystal lattice data.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import argparse
import sys

# script body for file processing
def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin, help='File to be parsed.')
	args = parser.parse_args()

	fileData = args.infile
	sourceFile = fileData.name

	dataSet = RemoveEmptyLattices(fileData)
	print(fileData.name + " has been processed successfully.")
	print("New dataset (raw):")
	print(dataSet)


# Removes empty [0,0,0] [h,k,l] lattices from the dataset
def RemoveEmptyLattices(sourceFile):
	data = []
	filteredData = []
	targetPath = ""
	lineIndex = 0

	for line in sourceFile:
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



# Call main function
if __name__ == "__main__":
	main()