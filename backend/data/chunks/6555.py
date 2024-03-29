@pytest.mark.usefixtures("mock_client_session_class")
@pytest.mark.asyncio
class FlaskRoutesTest(unittest.TestCase):
    """
    Need to mock some objects to control testing data locally
    Routes are hard to test regarding singleton app.
    Store all integration testcases in one class to ensure app context
    """

    def setUp(self):
        self.asgi_client = TestClient(APP)
        self.date = DATETIME_STRING

    def read_file_v1(self, state):
        filepath = "tests/expected_output/v1_{state}.json".format(state=state)
        with open(filepath, "r") as file:
            expected_json_output = file.read()
        return expected_json_output

    async def test_root_api(self):
        """Validate that / returns a 200 and is not a redirect."""
        response = await self.asgi_client.get("/")

        assert response.status_code == 200
        assert not response.is_redirect

    async def test_v1_confirmed(self):
        state = "confirmed"
        expected_json_output = self.read_file_v1(state=state)

        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = self.date
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            response = await self.asgi_client.get("/{}".format(state))

        return_data = response.json()
        assert return_data == json.loads(expected_json_output)

    async def test_v1_deaths(self):
        state = "deaths"
        expected_json_output = self.read_file_v1(state=state)

        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = self.date
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            response = await self.asgi_client.get("/{}".format(state))

        return_data = response.json()
        assert return_data == json.loads(expected_json_output)

    async def test_v1_recovered(self):
        state = "recovered"
        expected_json_output = self.read_file_v1(state=state)

        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = self.date
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            response = await self.asgi_client.get("/{}".format(state))

        return_data = response.json()
        assert return_data == json.loads(expected_json_output)

    async def test_v1_all(self):
        state = "all"
        expected_json_output = self.read_file_v1(state=state)

        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = self.date
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            response = await self.asgi_client.get("/{}".format(state))

        return_data = response.json()
        assert return_data == json.loads(expected_json_output)

    async def test_v2_latest(self):
        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = DATETIME_STRING
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            state = "latest"

            response = await self.asgi_client.get(f"/v2/{state}")

        return_data = response.json()
        check_dict = {"latest": {"confirmed": 1940, "deaths": 1940, "recovered": 0}}
        assert return_data == check_dict

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

    async def test_v2_locations_id(self):
        state = "locations"
        test_id = 1

        with mock.patch("app.services.location.jhu.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value.isoformat.return_value = DATETIME_STRING
            mock_datetime.strptime.side_effect = mocked_strptime_isoformat
            response = await self.asgi_client.get("/v2/{}/{}".format(state, test_id))

        return_data = response.json()

        filepath = "tests/expected_output/v2_{state}_id_{test_id}.json".format(
            state=state, test_id=test_id
        )
        with open(filepath, "r") as file:
            expected_json_output = file.read()

        assert return_data == json.loads(expected_json_output)