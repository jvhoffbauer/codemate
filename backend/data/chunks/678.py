def test_tutorial(clear_sqlmodel):
    from docs_src.tutorial.code_structure.tutorial002 import app, database

    database.sqlite_url = "sqlite://"
    database.engine = create_engine(database.sqlite_url)
    app.engine = database.engine
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        app.main()
    assert calls == expected_calls