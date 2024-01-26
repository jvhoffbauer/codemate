- Retrieves a user's profile from Couchbase using their email address
- Constructs an N1QL query with placeholders for `$type` and `$email`, which select all fields (including document ID) from the specified bucket where the `type` is equal to USERPROFILE_DOC_TYPE and the `email` matches the provided value
- Creates a `N1QLQuery` object with the constructed query string, specifying the bucket name, document type, and email parameter values
- Sets the consistency level of the query to REQUEST
- Executes the query against the bucket and returns the resulting documents in model format (converted by `utils.doc_results_to_model()`)
- If no matching documents are found, returns `None`.