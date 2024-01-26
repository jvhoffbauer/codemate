1. Creates a new Kite Connect session using the provided `request_token`.
2. Calculates and sets the SHA256 checksum for the API key, request token, and secret key.
3. Sends a POST request to the Kite Connect server with the necessary parameters and headers.
4. If successful, saves the access token to a local database and returns the LTP of the specified instrument.
5. Logs any errors encountered during session creation.