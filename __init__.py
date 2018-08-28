"""
This is a tool for creating various types of electronic 
calendar files. This is used to make it easy for people
to add a series of meetings to their work calendars without
having to worry about sharing your calendar and accidentally
altering it. 


Created by adam on 5/17/17

"""
__author__ = 'adam'


import os
import sys

ROOT = os.getenv("HOME")

# The folder containing environment.py
BASE = os.path.abspath(os.path.dirname(__file__))

# INPUTFOLDER = BASE + '/input'
# OUTPUTFOLDER = BASE + '/output'

# Source files
CALENDAR_TOOLS_PATH = "%s/CalendarHelpers" % BASE
sys.path.append(CALENDAR_TOOLS_PATH) #the directory that contains various common custom classes

#Test  folders
# TESTS_PATH = "%s/tests" % BASE
