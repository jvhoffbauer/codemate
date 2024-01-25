    def test_with_non_empty_string_and_str_type(self):
        result = validator_skip_blank("test", str)
        assert result == "test"