    def test_scalar_type_base_model(self):
        assert annotation_outer_type(MyModel) == MyModel
        assert annotation_outer_type(Optional[MyModel]) == MyModel