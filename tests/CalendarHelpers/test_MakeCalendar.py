import unittest

from MakeCalendar import *


class MakeCalendarTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_ics_event_file(self):
        e = Entry()
        self.assertTrue(create_ics_event_file(e), 'works with event')

    def test_create_ics_file_bad_input(self):
        e = []
        self.assertFalse(create_ics_event_file(e), 'does not work with non-event')


if __name__ == '__main__':
    unittest.main()
