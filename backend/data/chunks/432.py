def test_tutorial(clear_sqlmodel):
    from docs_src.tutorial.one import tutorial004_py310 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    with pytest.raises(MultipleResultsFound):
        mod.main()
    with Session(mod.engine) as session:
        # TODO: create delete() function
        # TODO: add overloads for .exec() with delete object
        session.exec(delete(mod.Hero))
        session.add(mod.Hero(name="Test Hero", secret_name="Secret Test Hero", age=24))
        session.commit()

    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.select_heroes()
    assert calls == [
        [
            "Hero:",
            {
                "id": 1,
                "name": "Test Hero",
                "secret_name": "Secret Test Hero",
                "age": 24,
            },
        ]
    ]