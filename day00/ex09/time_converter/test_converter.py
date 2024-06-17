# tests/test_converter.py
import unittest
from time_converter.converter import utc_to_local, local_to_utc, timestamp_to_datetime, datetime_to_timestamp
from datetime import datetime, timezone

class TestTimeConverter(unittest.TestCase):

    def test_utc_to_local(self):
        utc_dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        local_dt = utc_to_local(utc_dt)
        self.assertEqual(local_dt.year, 2021)

    def test_local_to_utc(self):
        local_dt = datetime(2021, 1, 1, 12, 0, 0)
        utc_dt = local_to_utc(local_dt)
        self.assertEqual(utc_dt.year, 2021)

    def test_timestamp_to_datetime(self):
        timestamp = 1609459200
        dt = timestamp_to_datetime(timestamp)
        self.assertEqual(dt.year, 2021)

    def test_datetime_to_timestamp(self):
        dt = datetime(2021, 1, 1, 12, 0, 0)
        timestamp = datetime_to_timestamp(dt)
        self.assertEqual(timestamp, 1609502400.0)

if __name__ == '__main__':
    unittest.main()
