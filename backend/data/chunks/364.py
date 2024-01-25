def test_nullable_primary_key(clear_sqlmodel, caplog):
    # Probably the weirdest corner case, it shouldn't happen anywhere, but let's test it
    class Hero(SQLModel, table=True):
        nullable_integer_primary_key: Optional[int] = Field(
            default=None,
            primary_key=True,
            nullable=True,
        )

    engine = create_engine("sqlite://", echo=True)
    SQLModel.metadata.create_all(engine)

    create_table_log = [
        message for message in caplog.messages if "CREATE TABLE hero" in message
    ][0]
    assert "nullable_integer_primary_key INTEGER," in create_table_log