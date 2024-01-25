def test_postgres_ddl_sql(capsys):
    SQLModel.metadata.create_all(bind=postgres_engine, checkfirst=False)

    captured = capsys.readouterr()
    assert "CREATE TYPE myenum1 AS ENUM ('A', 'B');" in captured.out
    assert "CREATE TYPE myenum2 AS ENUM ('C', 'D');" in captured.out