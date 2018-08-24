"""
Created by adam on 5/18/17
"""
__author__ = 'adam'
import sys
import unittest
import rednose

from CalendarHelpers.environment import *
# from environment import *
from CalendarHelpers.InputHandlers import *

TEST_FILE_NAME = 'calendar_input.csv'
TEST_FILE_PATH = '%s/%s' % (TESTS_PATH, TEST_FILE_NAME)

class CsvReaderTests( unittest.TestCase ):

    def setUp(self):
        self.object = CsvReader(TEST_FILE_PATH)

    def test_init(self):
        self.assertIsInstance(self.object, CsvReader, "Is csv reader")
        self.assertEqual(self.object.data_file_path, TEST_FILE_PATH)

    def test_load(self):
        expected_name = 'Senate'
        expected_location = 'Presentation room'
        expected_date = '20170601' #'6/1/17'
        expected_start_time = '14:00:00'
        expected_end_time = '16:30:00'

        result = self.object.load()

        #check that got the expected types of output
        self.assertIsInstance(result, list)
        for r in result:
            self.assertIsInstance(r, Event)

        result = result[0] # only 1 result

        self.assertEqual(expected_date, result.date)
        self.assertEqual(expected_name, result.name)
        self.assertEqual(expected_start_time, result.start)
        self.assertEqual(expected_end_time, result.end)
        self.assertEqual(expected_location, result.location)

        # for c in self.object.columns:
        #     self.assertTrue(c in result.keys(), "%s is in keys" % c)

        # print(result)
        # self.assertEqual(expected_date, result['date'])
        # self.assertEqual(expected_name, result['name'])
        # self.assertEqual(expected_start_time, result['start'])
        # self.assertEqual(expected_end_time, result['end'])
        # self.assertEqual(expected_location, result['location'])




if __name__ == '__main__':
    unittest.main( )
