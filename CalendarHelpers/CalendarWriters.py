"""
Created by adam on 5/17/17
"""
import ics
import CalendarHelpers.DataStructures

__author__ = 'adam'


class IcsMaker( object ):
    """Wraps the ics library to make a .ics file from the input data"""

    def __init__( self ):
        self.calendar = ics.Calendar()
        # Not sure why this is necessary. If do everything
        # the way it says in the docs, we get an error
        # because calendar.events is initially a set. Thus the
        # append step doesn't work. This alleviates the problem.
        self.calendar.events = [ ]

    def make_event( self, entry ):
        """Creates an ics.Event object from the provided entry"""
        e = ics.Event()
        e.name = entry.name
        e.begin = '%s %s' % (entry.date, entry.start)
        e.end = '%s %s' % (entry.date, entry.end)
        return e

    def add_event( self, entry: CalendarHelpers.DataStructures.Entry ):
        """Creates an entry from the entry and adds it to the calendar
        :type entry: CalendarHelpers.DataStructures.Entry
        """
        event = self.make_event( entry )
        self.calendar.events.append( event )

    def write_to_file( self, output_file_path ):
        with open( output_file_path, 'w' ) as my_file:
            my_file.writelines( self.calendar )


if __name__ == '__main__':
    pass
