# Description: Operations for creating and manipulating paths.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import os
import shutil

# Check for and write/overwrite to directory
def CreateDirectory(directory):
	if not os.path.exists(directory):
		print("Creating directory " + directory + " ...")
		os.mkdir(directory)
	else:
		print("Overwriting directory " + directory + " ...")
		shutil.rmtree(directory)
		os.mkdir(directory)

# Returns a newline tailored to the working environment
def Newline():
	ending = ""
	if os.name == "nt":
		ending = "\r\n"
	else:
		ending = "\n"
	return ending
