def test_depends_repr():
    assert repr(Depends()) == "Depends(NoneType)"
    assert repr(Depends(get_user)) == "Depends(get_user)"
    assert repr(Depends(use_cache=False)) == "Depends(NoneType, use_cache=False)"
    assert (
        repr(Depends(get_user, use_cache=False)) == "Depends(get_user, use_cache=False)"
    )