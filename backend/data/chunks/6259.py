    def test_with_enum_and_str_type_with_blank_member(self):
        class MyEnum(Enum):
            VALUE = "value"
            BLANK = ""

        result = validator_skip_blank("", MyEnum)
        assert result == ""