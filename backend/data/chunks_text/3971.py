- Tests GET request to `/timed` endpoint using Flask client
- Asserts that expected JSON response is returned with a specific message
- Verifies presence and validity of X-Response-Time header, which should contain a non-negative value representing server response time