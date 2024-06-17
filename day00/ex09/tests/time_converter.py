# time_converter/converter.py
from datetime import datetime, timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def local_to_utc(local_dt):
    return local_dt.astimezone(timezone.utc)

def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def datetime_to_timestamp(dt):
    return dt.timestamp()
