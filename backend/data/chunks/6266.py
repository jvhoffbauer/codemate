    def test_scalar_type_literal(self):
        assert annotation_outer_type(Literal[None, "a", "b"]) == str