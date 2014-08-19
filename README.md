synchrotools
=============

The synchrotools collection of scripts supply the materials scientist with tools for analyzing synchrotron beamline data, including (at current): separation of data by phase, filtration of [data] noise, filtration of empty detector readings, and a parsing mechanism that "zooms" into unique sets and extracts phase-specific readings to separate files for simplified inspection.

This software is a collaborative effort among [Nicola B. DiPalma](http://nicoladipalma.com/), [Oliver Tschauner, Ph.D.](http://geoscience.unlv.edu/people/olivertschauner.html), and scientists at the [University of Nevada, Las Vegas High Pressure Science and Engineering Center (HiPSEC)](http://hipsec.unlv.edu/). This software is intended to augment current data analysis capabilities at HiPSEC and is freely available through this repository for use by members of the scientific community.

Notes
-----

Code in this script has been composed in a self-documenting fashion and styled for readability where possible. Comments have been placed within source where readability is limited, and where functionality is a direct consequence of material esoteric to crystallographic study.

This version of the toolset was developed using Python version 3.x on Mac OSX v10.9.x; included modules have not yet been tested in the Microsoft Windows environment as of this writing.

Instructions for Use
--------------------

To use scripts included in this repository:

1. Install Python 3.x from [the Python website](https://www.python.org/) if you don't have it already.
2. Clone this repository to your machine.
3. Add the directory containing the cloned repository to your $PATH.
4. Then, enter the module you want to use in the terminal, with options (if any):
		$ python3 crystalid -s ~/Documents/ALS/March_2014/beamline_data.x_y

Terminal-enabled modules in this collection include:
		phaseid
		crystalid

All other modules serve as support for included functionality.

PhaseID is a tool for parsing a single beamline output file into constituent phases. This aids crystallographers in the task of locating the features for a particular phase instead of having to waste time inspecting integrated patterns visually. Proper use of this module is as follows:

		$ python3 phaseid [options] [input file]

If the module has not been set on the $PATH, the user must navigate to the directory containing the module script and run as follows:

		$ python3 phaseid.py [options] [input file]

CrystalID is a tool for filtering empty lattices and detector noise from crystallographic output data that allows scientists to spend less time sorting through data otherwise irrelevant to their studies. Proper use of this module is as follows:

		$ python3 crystalid [options] [input file]

If the module has not been set on the $PATH, the user must navigate to the directory containing the module script and run as follows:

		$ python3 crystalid.py [options] [input file]

A complete list of options and argumets for each module can be obtained from within the terminal by entering:

		$ python3 [module name/filename] --help

Instructions for Development
----------------------------

To get your machine ready for development with this repository:

1. Install Python 3.x from [the Python website](https://www.python.org/) if you don't have it already.
2. Clone this repository to your machine.
3. Navigate to the directory you cloned your repository to.
4. Open the repository in [IDLE](https://docs.python.org/3.4/library/idle.html), [Sublime Text](http://www.sublimetext.com/), or your favorite editor/development environment.

Viola! You're good to go!
