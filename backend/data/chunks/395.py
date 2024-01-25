def test_sa_relationship_property(clear_sqlmodel):
    """Test https://github.com/tiangolo/sqlmodel/issues/315#issuecomment-1272122306"""

    class Team(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str = Field(unique=True)
        heroes: List["Hero"] = Relationship(  # noqa: F821
            sa_relationship=RelationshipProperty("Hero", back_populates="team")
        )

    class Hero(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str = Field(unique=True)
        team_id: Optional[int] = Field(default=None, foreign_key="team.id")
        team: Optional[Team] = Relationship(
            sa_relationship=RelationshipProperty("Team", back_populates="heroes")
        )

    team_preventers = Team(name="Preventers")
    hero_rusty_man = Hero(name="Rusty-Man", team=team_preventers)

    engine = create_engine("sqlite://", echo=True)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(hero_rusty_man)
        session.commit()
        session.refresh(hero_rusty_man)
        # The next statement should not raise an AttributeError
        assert hero_rusty_man.team
        assert hero_rusty_man.team.name == "Preventers"