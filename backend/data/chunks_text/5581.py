- Defines a private method `_create_schema_update` that returns a type of SchemaUpdateT. - Sets default values for `update_fields` and `update_exclude`. - Filters out excluded fields and non-model fields from `update_fields`, then creates a new schema called "Update" with those remaining fields.