def create_db_and_tables():
    SQLModel.metadata.create_all(engine)  # (4)!