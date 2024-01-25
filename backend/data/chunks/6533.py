    def read_file(self, state):
        """
        Mock HTTP GET-method and return text from file
        """
        state = state.lower()

        # Determine filepath.
        filepath = os.path.join(
            os.path.dirname(__file__), "example_data/{}.csv".format(state)
        )

        # Return fake response.
        print("Try to read {}".format(filepath))
        with open(filepath, "r") as file:
            return file.read()