def delete_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Youngster")  # (1)!
        results = session.exec(statement)  # (2)!
        hero = results.one()  # (3)!
        print("Hero: ", hero)  # (4)!

        session.delete(hero)  # (5)!
        session.commit()  # (6)!

        print("Deleted hero:", hero)  # (7)!

        statement = select(Hero).where(Hero.name == "Spider-Youngster")  # (8)!
        results = session.exec(statement)  # (9)!
        hero = results.first()  # (10)!

        if hero is None:  # (11)!
            print("There's no hero named Spider-Youngster")  # (12)!
    # (13)!