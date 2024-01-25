    def test_scalar_type_list(self):
        assert annotation_outer_type(List[int]) == list