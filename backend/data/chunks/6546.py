def test_location_class(
    mocked_timeline,
    test_id,
    country,
    country_code,
    province,
    latitude,
    longitude,
    confirmed_latest,
    deaths_latest,
    recovered_latest,
):
    # id, country, province, coordinates, confirmed, deaths, recovered
    coords = coordinates.Coordinates(latitude=latitude, longitude=longitude)

    # Timelines
    confirmed = models.Timeline(confirmed_latest)
    deaths = models.Timeline(deaths_latest)
    recovered = models.Timeline(recovered_latest)

    # Date now.
    now = datetime.utcnow().isoformat() + "Z"

    # Location.
    location_obj = location.TimelinedLocation(
        test_id,
        country,
        province,
        coords,
        now,
        {
            "confirmed": confirmed,
            "deaths": deaths,
            "recovered": recovered,
        },
    )

    assert location_obj.country_code == country_code
    assert location_obj.serialize() is not None