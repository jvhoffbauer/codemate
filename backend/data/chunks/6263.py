    def test_scalar_type_union(self):
        assert annotation_outer_type(Union[int, str]) == int