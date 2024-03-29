def test_sa_column_args(clear_sqlmodel, caplog) -> None:
    class Team(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str

    class Hero(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        team_id: Optional[int] = Field(
            default=None,
            sa_column_args=[ForeignKey("team.id")],
        )

    engine = create_engine("sqlite://", echo=True)
    SQLModel.metadata.create_all(engine)
    create_table_log = [
        message for message in caplog.messages if "CREATE TABLE hero" in message
    ][0]
    assert "FOREIGN KEY(team_id) REFERENCES team (id)" in create_table_log