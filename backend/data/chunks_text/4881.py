1. Initializes Couchbase connection and sets configuration variables using `get_cluster_http_url`, `config_couchbase`, and environment variables (`COUCHBASE_USER`, `COUCHBASE_PASSWORD`, etc.).
2. Creates a bucket with specified name, RAM quota, and ensures its creation if it doesn't exist already using `ensure_create_bucket`.
3. Creates primary index for the newly created bucket using `ensure_create_primary_index`.
4. Creates type indexes for specific types of data in the bucket using `ensure_create_type_index`.
5. Creates full text search indexes based on definitions stored in a directory using `ensure_create_full_text_indexes`.
6. Syncs an existing Couchbase app user to the current Couchbase server using `ensure_create_couchbase_app_user_sync`.
7. Upserts a new user as the first superuser into the system using `crud.user.upsert()`.