@pytest.mark.asyncio
async def test_get_locations(mock_client_session):
    data = await csbs.get_locations()

    assert isinstance(data, list)

    # check to see that Unknown/Unassigned has been filtered
    for d in data:
        assert d.county != "Unknown"
        assert d.county != "Unassigned"