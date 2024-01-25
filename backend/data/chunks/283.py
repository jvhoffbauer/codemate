def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        result = session.exec(statement)
        hero_spider_boy = result.one()

        statement = select(Team).where(Team.id == hero_spider_boy.team_id)
        result = session.exec(statement)
        team = result.first()
        print("Spider-Boy's team:", team)

        print("Spider-Boy's team again:", hero_spider_boy.team)