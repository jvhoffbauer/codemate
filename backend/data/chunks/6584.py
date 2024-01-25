def mocked_csbs_requests_get(*args, **kwargs):
    class FakeRequestsGetResponse:
        """
        Returns instance of `FakeRequestsGetResponse`
        when calling `app.services.location.csbs.requests.get()
        """

        def __init__(self):
            self.text = self.read_file()

        def read_file(self):
            """
            Mock HTTP GET-method and return text from file
            """
            filepath = "tests/example_data/covid19_county.csv"
            print("Try to read {}".format(filepath))
            with open(filepath, "r") as file:
                return file.read()

    return FakeRequestsGetResponse()