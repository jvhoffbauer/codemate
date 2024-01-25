def test_is_date(str_date, fuzzy_bool, expected_value):
    """
    Testdata from https://stackoverflow.com/a/25341965/7120095
    """
    assert date.is_date(str_date, fuzzy=fuzzy_bool) is expected_value