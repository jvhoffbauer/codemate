- Defines a `User` model with an optional boolean field called `is_admin`.
- Uses Pydantic's `Field()` to specify that the default value for this field should be True and it has a custom label.
- Tests the functionality of Amis Form Builder by parsing the `is_admin` field as a form item (with default values), a filter item (without default values), and a table column. The tests verify that each parsed object has the correct type, label, and initial value.