def test_sa_column_no_primary_key() -> None:
    with pytest.raises(RuntimeError):

        class Item(SQLModel, table=True):
            id: Optional[int] = Field(
                default=None,
                primary_key=True,
                sa_column=Column(Integer, primary_key=True),
            )