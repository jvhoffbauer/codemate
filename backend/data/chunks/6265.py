    def test_scalar_type_ellipsis(self):
        assert annotation_outer_type(Ellipsis) == Any