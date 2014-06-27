# Description: Format functions for organizing raw data.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Keeps data columns uniform within each file - for readability
def FormatData(colWidth, leftJustifiedText):
	spaceLeft = 0
	stringLength = len(leftJustifiedText)
	whitespace = ""
	if colWidth > stringLength:
		spaceLeft = colWidth - stringLength
		for i in range(spaceLeft):
			whitespace += " "
	return leftJustifiedText + whitespace
