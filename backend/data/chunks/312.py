def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")  # (1)!
        results = session.exec(statement)  # (2)!
        hero = results.one()  # (3)!
        print("Hero:", hero)  # (4)!

        hero.age = 16  # (5)!
        session.add(hero)  # (6)!
        session.commit()  # (7)!
        session.refresh(hero)  # (8)!
        print("Updated hero:", hero)  # (9)!