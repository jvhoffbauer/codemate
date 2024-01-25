@pytest.mark.asyncio
@pytest.mark.parametrize(
    "query_params",
    [
        {"source": "csbs"},
        {"source": "jhu"},
        {"source": "nyt"},
        {"timelines": True},
        {"timelines": "true"},
        {"timelines": 1},
        {"source": "jhu", "timelines": True},
        {"source": "nyt", "timelines": True},
    ],
)
async def test_latest(async_api_client, query_params, mock_client_session):
    response = await async_api_client.get("/v2/latest", query_string=query_params)

    print(f"GET {response.url}\n{response}")

    response_json = response.json()
    print(f"\tjson:\n{pf(response_json)}")

    assert response.status_code == 200
    assert response_json["latest"]["confirmed"]
    assert response_json["latest"]["deaths"]