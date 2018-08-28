"""
Created by adam on 5/18/17
"""
__author__ = 'adam'

import unittest

from environment import *
# from environment import *

TEST_FILE_NAME = 'calendar_input.csv'
TEST_FILE_PATH = '%s/%s' % (TESTS_PATH, TEST_FILE_NAME)

class EventTests( unittest.TestCase ):

    def setUp(self):
        self.object = Event()

    def test_name(self):
        expected_name = 'Senate'

    def test_date(self):
        expected_date = '20170601' #'6/1/17'

    def test_start_time(self):
        expected_start_time = '14:00:00'

    def test_end_time(self):
        expected_end_time = '16:30:00'

    def test_location(self):
        expected_location = 'presentation room'

        # self.assertEqual(expected_date, result['date'])
        # self.assertEqual(expected_name, result['name'])
        # self.assertEqual(expected_start_time, result['start'])
        # self.assertEqual(expected_end_time, result['end'])
        # self.assertEqual(expected_location, result['location'])


if __name__ == '__main__':
    unittest.main( )
