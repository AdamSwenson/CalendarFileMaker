"""
Created by adam on 5/18/17
"""
__author__ = 'adam'

#
import os
# import sys
#
ROOT = os.getenv("HOME")
#
# # The folder containing environment.py
BASE = os.path.abspath(os.path.dirname(__file__))
#
INPUTFOLDER = BASE + '/input'
OUTPUTFOLDER = BASE + '/output'
#
# # Source files
# CALENDAR_TOOLS_PATH = "%s/CalendarHelpers" % BASE

# Test  folders
TESTS_PATH = "%s/tests" % BASE


# class Event(object):
#
#     def __init__(self):
#         self._name
#         self._start
#         self._end
#         self.location
#
#     @property
#     def name(self, name):
#         self._name = name
#
#     @name.getter
#     def nameget(self):
#         return self._name
