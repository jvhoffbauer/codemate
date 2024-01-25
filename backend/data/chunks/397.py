def sqlite_dump(sql: TypeEngine, *args, **kwargs):
    dialect = sql.compile(dialect=sqlite_engine.dialect)
    sql_str = str(dialect).rstrip()
    if sql_str:
        print(sql_str + ";")