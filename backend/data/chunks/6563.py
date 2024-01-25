    async def test_v2_latest(self):
        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = DATETIME_STRING
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            state = "latest"

            response = await self.asgi_client.get(f"/v2/{state}")

        return_data = response.json()
        check_dict = {"latest": {"confirmed": 1940, "deaths": 1940, "recovered": 0}}
        assert return_data == check_dict