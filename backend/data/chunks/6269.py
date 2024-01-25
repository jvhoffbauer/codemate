    def test_scalar_type_dict(self):
        assert annotation_outer_type(Dict[str, int]) == dict