def test_parse_history(key, locations, index, expected):
    """
    Test validating and extracting history content from
    locations data based on index.
    """
    assert jhu.parse_history(key, locations, index) == expected