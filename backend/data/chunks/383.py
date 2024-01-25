def test_sa_column_no_sa_kargs() -> None:
    with pytest.raises(RuntimeError):

        class Item(SQLModel, table=True):
            id: Optional[int] = Field(
                default=None,
                sa_column_kwargs={"primary_key": True},
                sa_column=Column(Integer, primary_key=True),
            )