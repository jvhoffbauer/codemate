- Defines a custom `ArticleCrud` using SQLAlchemyCrud and registers it with the application's router.
- Adds four fields to the `list_filter`, including two related fields from another table (`User`) using outer joins.
- Tests that the correct fields are included in the schema filter and OpenAPI documentation.
- Makes API requests with different filters and verifies that the expected results are returned.