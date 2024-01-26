- Defines a new `UserStatus` enum using Django's built-in `IntegerChoices` for integer values and custom string labels. - Asserts that the outer type of this enum (i.e., its metaclass) is equal to itself (`UserStatus`) using Python's `annotation_outer_type()` function from PEP 560. This ensures that the enum behaves as expected when used in annotations or return types.