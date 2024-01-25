def test_sa_column_kargs(clear_sqlmodel, caplog) -> None:
    class Item(SQLModel, table=True):
        id: Optional[int] = Field(
            default=None,
            sa_column_kwargs={"primary_key": True},
        )

    engine = create_engine("sqlite://", echo=True)
    SQLModel.metadata.create_all(engine)
    create_table_log = [
        message for message in caplog.messages if "CREATE TABLE item" in message
    ][0]
    assert "PRIMARY KEY (id)" in create_table_log