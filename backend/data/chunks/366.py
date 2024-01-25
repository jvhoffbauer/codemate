def test_not_allow_instantiation_without_arguments_if_not_table():
    class Item(SQLModel):
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str
        description: Optional[str] = None

    with pytest.raises(ValidationError):
        Item()