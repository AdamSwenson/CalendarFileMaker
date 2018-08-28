"""
Created by adam on 5/18/17
"""
__author__ = 'adam'

import datetime


class Entry(object):
    """File readers will create instances of these objects.
    Calendar makers will consume them"""

    def __init__(self):
        self._name = ''
        self._date = ''
        self._start = ''
        self._end = ''
        self._location = ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = DataFormattingHelper.make_name( name )

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = DataFormattingHelper.make_date( date )

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start_time):
        self._start = DataFormattingHelper.make_time( start_time )

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end_time):
        self._end = DataFormattingHelper.make_time( end_time )

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = DataFormattingHelper.make_name(location)


class DataFormattingHelper( object ):
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