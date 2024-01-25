def get_engine_db(engine: SqlalchemyDatabase) -> Union[Database, AsyncDatabase]:
    if isinstance(engine, (Database, AsyncDatabase)):
        return engine
    if isinstance(engine, Engine):
        return Database(engine)
    if isinstance(engine, AsyncEngine):
        return AsyncDatabase(engine)
    raise TypeError(f"Unknown engine type: {type(engine)}")