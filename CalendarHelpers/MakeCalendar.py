"""
Created by adam on 5/17/17
"""
__author__ = 'adam'

# standard lib

import ics

from InputHandlers import *

input_file_path = '%s/upbg-calendar-1718.csv' % INPUTFOLDER
output_file_path = '%s/cal.ics' % OUTPUTFOLDER


class IcsWrapper(object):
    def __init__(self):
        self.calendar = ics.Calendar()

    def add_event(self, event):
        e = ics.Event()
        e.name = event.name
        e.begin = '%s %s' % (event.date, event.start)
        e.end = '%s %s' % (event.date, event.end)
        self.calendar.events.append(e)

    def write_to_file(self, output_file_path=output_file_path):
        with open(output_file_path, 'w') as my_file:
            my_file.writelines(self.calendar)


#
# """
# >>> from ics import Calendar, Entry
# >>> c = Calendar()
# >>> e = Entry()
# >>> e.name = "My cool event"
# >>> e.begin = '20140101 00:00:00'
# >>> c.events.append(e)
# >>> c.events
# [<Entry 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
# >>> with open('my.ics', 'w') as my_file:
#     >>>     my_file.writelines(c)
# >>> # and it's done !
# """
# def create_ics_event_file(event, output_file_path=output_file_path ):
#     assert( isinstance(event, Event))
#     c = ics.Calendar()
#     e = ics.Event()
#     e.name = Event.name
#     e.begin = '%s %s' % (Event.date, Event.start)
#     e.end = '%s %s' % (Event.date, Event.end)
#
#
if __name__ == '__main__':

    # read the calendar dates from file
    reader = CsvReader(input_file_path)
    # process into standard format
    loaded = reader.load()
    # write to formats
    cal = IcsWrapper()
    for e in loaded:
        cal.add_event(e)
    cal.write_to_file(output_file_path)
