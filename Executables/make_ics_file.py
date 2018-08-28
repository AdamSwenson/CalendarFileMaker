"""
Created by adam on 5/17/17
"""
__author__ = 'adam'

import environment
from CalendarHelpers.CalendarWriters import IcsMaker
import CalendarHelpers.FileSystemTools as FST
from CalendarHelpers.InputHandlers import CsvReader

# input_file_path = '%s/upbg-calendar-1718.csv' % environment.INPUTFOLDER
output_file_path = '%s/cal.ics' % environment.OUTPUTFOLDER

if __name__ == '__main__':
    files = [ ]
    loaded_data = [ ]
    dfi = FST.makeDataFileIterator( environment.INPUTFOLDER )
    try:
        while True:
            f = next( dfi )
            if f[ -4: ] == '.csv':
                print( "Loading events from %s" % f )
                # read the calendar dates from file
                reader = CsvReader( f )
                # process into standard format
                loaded_data += reader.load()
    except StopIteration:
        # write to formats
        cal = IcsMaker()
        [ cal.add_event( e ) for e in loaded_data ]
        cal.write_to_file( output_file_path )
        print( "Wrote %s events to %s" % (len( loaded_data ), output_file_path) )
