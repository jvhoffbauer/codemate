def create_db_and_tables():  # (11)!
    SQLModel.metadata.create_all(engine)  # (12)!