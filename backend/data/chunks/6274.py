def test_annotation_utils():
    assert field_annotation_is_scalar(str) is True
    assert field_annotation_is_scalar(int) is True
    assert field_annotation_is_scalar(datetime) is True
    assert field_annotation_is_scalar(Optional[str]) is True
    assert field_annotation_is_scalar(Optional[datetime]) is True
    assert field_annotation_is_scalar(Union[datetime, date]) is True
    assert field_annotation_is_scalar_sequence(List[str]) is True
    assert field_annotation_is_scalar_sequence(Set[str]) is True
    assert field_annotation_is_scalar_sequence(list) is True
    assert field_annotation_is_scalar_sequence(tuple) is True
    assert field_annotation_is_scalar_sequence(Optional[Set[str]]) is True
    assert field_annotation_is_scalar(MyModel) is False
    assert field_annotation_is_complex(list) is True
    assert field_annotation_is_complex(MyModel) is True
    assert field_annotation_is_complex(dict) is True
    assert field_annotation_is_complex(Dict[str, Any]) is True
    assert get_origin(Literal[42, 43]) is Literal
    assert get_origin(int) is None
    assert get_origin(Optional[int]) is Union
    assert get_origin(Union[int, str]) is Union
    assert field_annotation_is_sequence(List[str]) is True
    assert field_annotation_is_sequence(List[MyModel]) is True