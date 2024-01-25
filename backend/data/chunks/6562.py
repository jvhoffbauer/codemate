    async def test_v1_all(self):
        state = "all"
        expected_json_output = self.read_file_v1(state=state)

        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = self.date
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            response = await self.asgi_client.get("/{}".format(state))

        return_data = response.json()
        assert return_data == json.loads(expected_json_output)