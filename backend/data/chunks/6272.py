    def test_scalar_type_annotated(self):
        assert annotation_outer_type(Annotated[int, "123"]) == int
        assert annotation_outer_type(Annotated[Optional[int], "123"]) == int
        assert annotation_outer_type(Annotated[List[int], "123"]) == list