"""
This makes one ics file for each of the csv files it
consumes
Created by adam on 5/17/17
"""
__author__ = 'adam'

import environment
from CalendarHelpers.CalendarWriters import IcsMaker
import CalendarHelpers.FileSystemTools as FST
from CalendarHelpers.InputHandlers import CsvReader


if __name__ == '__main__':
    dfi = FST.makeDataFileIterator( environment.INPUTFOLDER )
    try:
        while True:
            f = next( dfi )
            if f[ -4: ] == '.csv':
                print( "Loading events from %s" % f )
                # read the calendar dates from file
                reader = CsvReader( f )
                loaded_data = reader.load()

                input_file_name = f.split('/')[-1:][0][:-4]
                print(input_file_name)
                output_file_path = "%s/%s.ics" % (environment.OUTPUTFOLDER, input_file_name)

                cal = IcsMaker()
                [ cal.add_event( e ) for e in loaded_data ]
                cal.write_to_file( output_file_path )
                print( "Wrote %s events to %s" % (len( loaded_data ), output_file_path) )

    except StopIteration:
        # write to formats
        print("Done processing")
