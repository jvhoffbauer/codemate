def test_fetch_populations(body_arg, json_arg):
    responses.add(
        responses.GET, app.utils.populations.GEONAMES_URL, body=body_arg, json=json_arg
    )

    assert app.utils.populations.fetch_populations()