async def test_get_locations(mock_client_session):
    with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value.isoformat.return_value = DATETIME_STRING
        mock_datetime.strptime.side_effect = mocked_strptime_isoformat
        output = await jhu.get_locations()

    assert isinstance(output, list)
    assert isinstance(output[0], location.Location)

    # `jhu.get_locations()` creates id based on confirmed list
    location_confirmed = await jhu.get_category("confirmed")
    assert len(output) == len(location_confirmed["locations"])

    # `jhu.get_locations()` creates id based on deaths list
    location_deaths = await jhu.get_category("deaths")
    assert len(output) == len(location_deaths["locations"])

    # `jhu.get_locations()` creates id based on recovered list
    location_recovered = await jhu.get_category("recovered")
    assert len(output) == len(location_recovered["locations"])