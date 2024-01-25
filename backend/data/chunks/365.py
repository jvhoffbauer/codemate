def test_allow_instantiation_without_arguments(clear_sqlmodel):
    class Item(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str
        description: Optional[str] = None

    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as db:
        item = Item()
        item.name = "Rick"
        db.add(item)
        db.commit()
        statement = select(Item)
        result = db.exec(statement).all()
    assert len(result) == 1
    assert isinstance(item.id, int)
    SQLModel.metadata.clear()