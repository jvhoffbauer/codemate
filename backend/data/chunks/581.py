@needs_py310
def test_tutorial_001(clear_sqlmodel):
    from docs_src.tutorial.automatic_id_none_refresh import tutorial001_py310 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()
    check_calls(calls)