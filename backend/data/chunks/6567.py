async def test_locations_status_code(
    async_api_client, query_params, expected_status, mock_client_session
):
    response = await async_api_client.get("/v2/locations", query_string=query_params)

    print(f"GET {response.url}\n{response}")
    print(f"\tjson:\n{pf(response.json())[:1000]}\n\t...")
    assert response.status_code == expected_status