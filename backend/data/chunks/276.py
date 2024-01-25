def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age < 25)
        results = session.exec(statement)
        hero = results.first()
        print("Hero:", hero)