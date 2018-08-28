"""
Created by adam on 5/18/17
"""
__author__ = 'adam'

import datetime

from . import InputHandlers

class Entry(object):

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
        self._name = self.make_name(name)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = InputHandlers.InputDataHandler.make_date( date )

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start_time):
        self._start = InputHandlers.InputDataHandler.make_time( start_time )

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end_time):
        self._end = InputHandlers.InputDataHandler.make_time( end_time )

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = self.make_name(location)


    # def make_date(self, date_string):
    #     """
    #     Processes the imported date of the event into the
    #     expected date format
    #     Expected format: YYYYMMDD
    #     """
    #     # return date_string
    #     if(date_string != 'date'):
    #         d = [int(i) for i in date_string.split('/')]
    #         y = int("20%s" % d[2])
    #
    #         # m = int()
    #         dt = datetime.date(y, d[0], d[1])
    #         return dt.strftime("%Y%m%d")
    #     # return '%s%s%s' % (dt.year, dt.month, dt.day)
    #
    # def make_time(self, time_string):
    #     """
    #     Process the imported time of the event into the
    #     expected time format
    #     00:00:00
    #     """
    #     hh = time_string[:2] if len(time_string) > 1 else '00'
    #     mm = time_string[2:4] if len(time_string) > 2 else '00'
    #     return '%s:%s:00' % (hh,mm)

    def make_name(self, input_name):
        """
        Process the imported name into the expected formatting
        :param input_name: 
        :return: 
        """
        return input_name.capitalize()
