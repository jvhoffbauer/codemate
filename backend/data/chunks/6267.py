    def test_scalar_type_enum(self):
        class MyEnum(Enum):
            VALUE = "value"

        assert annotation_outer_type(MyEnum) == MyEnum

        assert annotation_outer_type(Optional[MyEnum]) == MyEnum