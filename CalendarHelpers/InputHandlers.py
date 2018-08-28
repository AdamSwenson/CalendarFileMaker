"""
Created by adam on 5/17/17
"""
__author__ = 'adam'

from CalendarHelpers.DataStructures import Entry
import csv
import datetime


class InputDataHandler(object):
    """Parent class of all tools for reading calendar data
    from a file
    """

    def __init__(self):
        pass

    @staticmethod
    def make_date(date_string):
        """
        Processes the imported date of the event into the
        date format other stuff will expect
        Expected format: YYYYMMDD
        Args:
            date_string: Format M/D/YY
        """
        # return date_string
        d = [int(i) for i in date_string.split('/')]
        y = int("20%s" % d[2])

        # m = int()
        dt = datetime.date(y, d[0], d[1])
        return dt.strftime("%Y%m%d")
        # return '%s%s%s' % (dt.year, dt.month, dt.day)

    @staticmethod
    def make_time(time_string):
        """
        Process the imported time of the event into the 
        expected time format
        00:00:00
        """
        hh = time_string[:2] if len(time_string) > 1 else '00'
        mm = time_string[2:4] if len(time_string) > 2 else '00'
        return '%s:%s:00' % (hh,mm)

    @staticmethod
    def make_name(input_name):
        """
        Process the imported name into the expected formatting
        :param input_name: 
        :return: 
        """
        return input_name.capitalize()

    def load(self):
        """
        Loads data from a file
        Returns a list of Entry objects
        """
        raise NotImplementedError


class CsvReader(InputDataHandler):
    def __init__(self, data_file_path):
        super().__init__()
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
                    except Exception:
                        print("Could not capture %s %s" % (row['name'], row['date']))

                    # row['name'] = self.make_name(row['name'])
                    # row['date'] = self.make_date(row['date'])
                    # row['start'] = self.make_time(row['start'])
                    # row['end'] = self.make_time(row['end'])

            # out = out[1:] if len(out) == 2 else out

        return out




if __name__ == '__main__':
    pass
