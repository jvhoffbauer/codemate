- Tests deleting a specific job with given ID and superuser token headers
- Sends a POST request to /job/del endpoint with job ID in JSON body and superuser token as headers
- Verifies that server returns HTTP status code 200 and success message (JSON object with "code" key equal to 200)