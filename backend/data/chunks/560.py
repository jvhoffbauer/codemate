def test_tutorial(clear_sqlmodel):
    from docs_src.tutorial.relationship_attributes.create_and_update_relationships import (
        tutorial001_py310 as mod,
    )

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()
    assert calls == expected_calls