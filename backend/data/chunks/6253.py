    def test_with_empty_string_and_int_type(self):
        result = validator_skip_blank("", int)
        assert result is None