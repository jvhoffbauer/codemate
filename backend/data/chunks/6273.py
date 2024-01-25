def test_scalar_sequence_inner_type():
    assert scalar_sequence_inner_type(List[int]) == int
    assert scalar_sequence_inner_type(List[MyModel]) == MyModel
    assert scalar_sequence_inner_type(List[Optional[MyModel]]) == MyModel
    assert scalar_sequence_inner_type(list) == Any
    assert scalar_sequence_inner_type(List[Union[str, int]]) == str
    assert scalar_sequence_inner_type(Annotated[List[Union[str, int]], "123"]) == str