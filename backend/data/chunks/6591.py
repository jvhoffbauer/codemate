@responses.activate
@pytest.mark.parametrize(
    "body_arg, json_arg",
    [
        (None, SAMPLE_GEONAMES_JSON),
        (NOT_FOUND_HTML, None),
        (None, {"foo": "bar"}),
        (requests.exceptions.Timeout("Forced Timeout"), None),
    ],
)
def test_fetch_populations(body_arg, json_arg):
    responses.add(
        responses.GET, app.utils.populations.GEONAMES_URL, body=body_arg, json=json_arg
    )

    assert app.utils.populations.fetch_populations()