    def test_with_enum_and_str_type(self):
        class MyEnum(Enum):
            VALUE = "value"

        result = validator_skip_blank("", MyEnum)
        assert result is None