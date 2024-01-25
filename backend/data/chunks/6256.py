    def test_with_integer_and_str_type(self):
        result = validator_skip_blank(123, str)
        assert result == "123"