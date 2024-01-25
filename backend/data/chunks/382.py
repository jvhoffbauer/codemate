def test_sa_column_no_sa_args() -> None:
    with pytest.raises(RuntimeError):

        class Item(SQLModel, table=True):
            id: Optional[int] = Field(
                default=None,
                sa_column_args=[Integer],
                sa_column=Column(Integer, primary_key=True),
            )