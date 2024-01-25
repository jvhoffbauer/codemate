    def test_scalar_type_optional(self):
        assert annotation_outer_type(Optional[int]) == int