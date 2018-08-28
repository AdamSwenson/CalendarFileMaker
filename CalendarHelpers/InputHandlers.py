"""
Created by adam on 5/17/17
"""

__author__ = 'adam'
from CalendarHelpers.DataStructures import Entry
import csv


class CsvReader( object ):
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.columns = ('name', 'date', 'start', 'end', 'location')

    def load(self):
        out = []

        with open(self.data_file_path) as csvFile:
            reader = csv.DictReader(csvFile, fieldnames=self.columns, quotechar='|')
            for row in reader:
                if row['name'] not in self.columns:
                    try:
                        event = Entry()
                        event.name = row['name']
                        event.date = row['date']
                        event.start = row['start']
                        event.end = row['end']
                        event.location = row['location']
                        out.append(event)
                    except Exception as e:
                        # print(e)
                        print("Could not capture %s %s" % (row['name'], row['date']))

                    # row['name'] = self.make_name(row['name'])
                    # row['date'] = self.make_date(row['date'])
                    # row['start'] = self.make_time(row['start'])
                    # row['end'] = self.make_time(row['end'])

            # out = out[1:] if len(out) == 2 else out

        return out




if __name__ == '__main__':
    pass
