- Creates a new task with specific start and end dates, repeat interval, and process delay using PUT request to /items endpoint
- Extracts necessary information from the response body and updates it with calculated values such as start_process and duration
- Asserts that the status code is 200 (OK), and compares the actual response JSON with an updated version of the input data