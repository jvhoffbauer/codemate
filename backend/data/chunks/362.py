def test_nullable_fields(clear_sqlmodel, caplog):
    class Hero(SQLModel, table=True):
        primary_key: Optional[int] = Field(
            default=None,
            primary_key=True,
        )
        required_value: str
        optional_default_ellipsis: Optional[str] = Field(default=...)
        optional_default_none: Optional[str] = Field(default=None)
        optional_non_nullable: Optional[str] = Field(
            nullable=False,
        )
        optional_nullable: Optional[str] = Field(
            nullable=True,
        )
        optional_default_ellipses_non_nullable: Optional[str] = Field(
            default=...,
            nullable=False,
        )
        optional_default_ellipses_nullable: Optional[str] = Field(
            default=...,
            nullable=True,
        )
        optional_default_none_non_nullable: Optional[str] = Field(
            default=None,
            nullable=False,
        )
        optional_default_none_nullable: Optional[str] = Field(
            default=None,
            nullable=True,
        )
        default_ellipses_non_nullable: str = Field(default=..., nullable=False)
        optional_default_str: Optional[str] = "default"
        optional_default_str_non_nullable: Optional[str] = Field(
            default="default", nullable=False
        )
        optional_default_str_nullable: Optional[str] = Field(
            default="default", nullable=True
        )
        str_default_str: str = "default"
        str_default_str_non_nullable: str = Field(default="default", nullable=False)
        str_default_str_nullable: str = Field(default="default", nullable=True)
        str_default_ellipsis_non_nullable: str = Field(default=..., nullable=False)
        str_default_ellipsis_nullable: str = Field(default=..., nullable=True)

    engine = create_engine("sqlite://", echo=True)
    SQLModel.metadata.create_all(engine)

    create_table_log = [
        message for message in caplog.messages if "CREATE TABLE hero" in message
    ][0]
    assert "primary_key INTEGER NOT NULL," in create_table_log
    assert "required_value VARCHAR NOT NULL," in create_table_log
    assert "optional_default_ellipsis VARCHAR," in create_table_log
    assert "optional_default_none VARCHAR," in create_table_log
    assert "optional_non_nullable VARCHAR NOT NULL," in create_table_log
    assert "optional_nullable VARCHAR," in create_table_log
    assert (
        "optional_default_ellipses_non_nullable VARCHAR NOT NULL," in create_table_log
    )
    assert "optional_default_ellipses_nullable VARCHAR," in create_table_log
    assert "optional_default_none_non_nullable VARCHAR NOT NULL," in create_table_log
    assert "optional_default_none_nullable VARCHAR," in create_table_log
    assert "default_ellipses_non_nullable VARCHAR NOT NULL," in create_table_log
    assert "optional_default_str VARCHAR," in create_table_log
    assert "optional_default_str_non_nullable VARCHAR NOT NULL," in create_table_log
    assert "optional_default_str_nullable VARCHAR," in create_table_log
    assert "str_default_str VARCHAR NOT NULL," in create_table_log
    assert "str_default_str_non_nullable VARCHAR NOT NULL," in create_table_log
    assert "str_default_str_nullable VARCHAR," in create_table_log
    assert "str_default_ellipsis_non_nullable VARCHAR NOT NULL," in create_table_log
    assert "str_default_ellipsis_nullable VARCHAR," in create_table_log