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

	RemoveEmptyLattices(fileData)


# Removes 0,0,0 hkl lattices from the dataset
def RemoveEmptyLattices(sourceFile):
	lineOfData = []
	targetPath = ""
	lineIndex = 0

	for line in sourceFile:
		if lineIndex > 1:
			lineOfData = line.split(',')
			for data in lineOfData:
				if data[0].strip() != "0" and data[1].strip() != "0" and data[2].strip() != "0":
					print(line)	

		lineIndex += 1


# Call main function
if __name__ == "__main__":
	main()