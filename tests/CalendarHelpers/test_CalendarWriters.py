import unittest

from CalendarHelpers.CalendarWriters import IcsMaker


class IcsMakerTests(unittest.TestCase):
    def setUp(self):
        self.obj = IcsMaker()

    def test_make_event(self):
        self.assertTrue(create_ics_event_file(e), 'works with event')


if __name__ == '__main__':
    unittest.main()
