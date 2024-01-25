def test_non_nullable_optional_field_with_no_default_set(clear_sqlmodel, caplog):
    class Hero(SQLModel, table=True):
        primary_key: Optional[int] = Field(
            default=None,
            primary_key=True,
        )

        optional_non_nullable_no_default: Optional[str] = Field(nullable=False)

    engine = create_engine("sqlite://", echo=True)
    SQLModel.metadata.create_all(engine)

    create_table_log = [
        message for message in caplog.messages if "CREATE TABLE hero" in message
    ][0]
    assert "primary_key INTEGER NOT NULL," in create_table_log
    assert "optional_non_nullable_no_default VARCHAR NOT NULL," in create_table_log

    # We can create a hero with `None` set for the optional non-nullable field
    hero = Hero(primary_key=123, optional_non_nullable_no_default=None)
    # But we cannot commit it.
    with Session(engine) as session:
        session.add(hero)
        with pytest.raises(IntegrityError):
            session.commit()