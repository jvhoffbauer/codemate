def test_countries_country_name__country_code(country_name, expected_country_code):
    assert countries.country_code(country_name) == expected_country_code