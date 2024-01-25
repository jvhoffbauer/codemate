def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 1)
        results = session.exec(statement)
        hero = results.first()
        print("Hero:", hero)