def test_type_list_breaks() -> None:
    with pytest.raises(ValueError):

        class Hero(SQLModel, table=True):
            id: Optional[int] = Field(default=None, primary_key=True)
            tags: List[str]