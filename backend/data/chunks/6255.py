    def test_with_non_empty_string_and_int_type(self):
        result = validator_skip_blank("123", int)
        assert result == 123