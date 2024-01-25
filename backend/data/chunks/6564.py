    async def test_v2_locations(self):
        state = "locations"

        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = DATETIME_STRING
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            response = await self.asgi_client.get("/v2/{}".format(state))

        return_data = response.json()

        filepath = "tests/expected_output/v2_{state}.json".format(state=state)
        with open(filepath, "r") as file:
            expected_json_output = file.read()

        assert return_data == json.loads(expected_json_output)