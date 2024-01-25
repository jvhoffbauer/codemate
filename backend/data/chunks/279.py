def update_heroes():
    with Session(engine) as session:
        hero_spider_boy = session.exec(
            select(Hero).where(Hero.name == "Spider-Boy")
        ).one()

        preventers_team = session.exec(
            select(Team).where(Team.name == "Preventers")
        ).one()

        print("Hero Spider-Boy:", hero_spider_boy)
        print("Preventers Team:", preventers_team)
        print("Preventers Team Heroes:", preventers_team.heroes)

        hero_spider_boy.team = None

        print("Spider-Boy without team:", hero_spider_boy)

        print("Preventers Team Heroes again:", preventers_team.heroes)

        session.add(hero_spider_boy)
        session.commit()
        print("After committing")

        session.refresh(hero_spider_boy)
        print("Spider-Boy after commit:", hero_spider_boy)

        print("Preventers Team Heroes after commit:", preventers_team.heroes)