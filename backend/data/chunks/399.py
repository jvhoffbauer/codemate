def test_sqlite_ddl_sql(capsys):
    SQLModel.metadata.create_all(bind=sqlite_engine, checkfirst=False)

    captured = capsys.readouterr()
    assert "enum_field VARCHAR(1) NOT NULL" in captured.out
    assert "CREATE TYPE" not in captured.out