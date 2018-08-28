"""
Created by adam on 5/17/17
"""
import ics

__author__ = 'adam'


class CalendarFileWriter(object):
    """
    Parent class for all tools which write to calendar file formats
    
    """
    def __init__(self):
        pass



if __name__ == '__main__':
    pass


class IcsMaker( object ):
    """Wraps an ics.Calendar"""

    def __init__( self ):
        self.calendar = ics.Calendar()
        # Not sure why this is necessary. If do everything
        # the way it says in the docs, we get an error
        # because calendar.events is initially a set. Thus the
        # append step doesn't work. This alleviates the problem.
        self.calendar.events = [ ]

    def make_event( self, data ):
        """Creates an ics.Event object from the provided data"""
        e = ics.Event()
        e.name = data.name
        e.begin = '%s %s' % (data.date, data.start)
        e.end = '%s %s' % (data.date, data.end)
        return e

    def add_event( self, data ):
        """Creates an data from the data and adds it to the calendar"""
        event = self.make_event( data )
        self.calendar.events.append( event )

    def write_to_file( self, output_file_path ):
        with open( output_file_path, 'w' ) as my_file:
            my_file.writelines( self.calendar )