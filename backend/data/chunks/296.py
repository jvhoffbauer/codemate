def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where((Hero.age <= 35) | (Hero.age > 90))
        results = session.exec(statement)
        for hero in results:
            print(hero)