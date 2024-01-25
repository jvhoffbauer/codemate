@pytest.mark.parametrize(
    "key, locations, index, expected",
    [
        (
            ("Thailand", "TH"),
            [{"country": "Thailand", "province": "TH", "history": {"test": "yes"}}],
            0,
            {"test": "yes"},
        ),  # Success
        (
            ("Deutschland", "DE"),
            [{"country": "Deutschland", "province": "DE", "history": {"test": "no"}}],
            1,
            {},
        ),  # IndexError
        (
            ("US", "NJ"),
            [{"country": "Deutschland", "province": "DE", "history": {"test": "no"}}],
            0,
            {},
        ),  # Invaid Key Merge
    ],
)
def test_parse_history(key, locations, index, expected):
    """
    Test validating and extracting history content from
    locations data based on index.
    """
    assert jhu.parse_history(key, locations, index) == expected