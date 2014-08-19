synchrotools
=============

The synchrotools collection of scripts supply the materials scientist with tools for analyzing synchrotron beamline data, including (at current): separation of data by phase, filtration of [data] noise, filtration of empty detector readings, and a parsing mechanism that "zooms" into unique sets and extracts phase-specific readings to separate files for simplified inspection.

This software is a collaborative effort among [Nicola B. DiPalma](http://nicoladipalma.com/), [Oliver Tschauner, Ph.D.](http://geoscience.unlv.edu/people/olivertschauner.html), and scientists at the [University of Nevada, Las Vegas High Pressure Science and Engineering Center (HiPSEC)](http://hipsec.unlv.edu/). This software is intended to augment current data analysis capabilities at HiPSEC and is freely available through this repository for use by members of the scientific community.

Notes
-----

Code in this script has been composed in a self-documenting fashion and styled for readability where possible. Comments have been placed within source where readability is limited, and where functionality is a direct consequence of material esoteric to crystallographic study.

This version of the toolset was developed using Python version 3.x on Mac OSX v10.9.x; included modules have not yet been tested in the Microsoft Windows environment as of this writing.

Instructions
------------

To get your machine ready for development with this repository:

1. Install python 3.x from [the Python website](https://www.python.org/)
2. Clone the repository to your machine.
3. Navigate to the directory you cloned your repository to.
4. Then, enter the module you want to use in the terminal, with options:

		$ python3 crystalid -s ~/Documents/ALS/March_2014/beamline_data.x_y

Viola! You're good to go!
