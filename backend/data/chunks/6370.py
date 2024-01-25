def prepare_database(models) -> Generator[None, None, None]:
    models.Base.metadata.create_all(db.engine)
    yield
    models.Base.metadata.drop_all(db.engine)