def test_tutorial(clear_sqlmodel):
    from docs_src.tutorial.where import tutorial001 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()
    assert calls == [
        [
            {
                "name": "Deadpond",
                "secret_name": "Dive Wilson",
                "age": None,
                "id": 1,
            }
        ]
    ]