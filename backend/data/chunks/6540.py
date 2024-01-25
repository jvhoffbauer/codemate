def mocked_strptime_isoformat(*args, **kwargs):
    """Mock return value from datetime.strptime().isoformat()."""

    date = args[0]
    strformat = args[1]

    return DateTimeStrpTime(date, strformat)