- Establishes a connection to Couchbase Server using the `Cluster()` constructor and passing in the server's URL, fetching mutation tokens, setting operation timeout, and N1QL query timeout. - Authenticates with the specified username and password using the `PasswordAuthenticator()`. - Opens the desired bucket named 'bucket_name', specifying wait mode for locks (LOCKMODE_WAIT). - Sets timeouts for both operations and N1QL queries within the opened bucket.