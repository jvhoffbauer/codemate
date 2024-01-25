def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")  # (1)!
        results = session.exec(statement)  # (2)!
        hero_1 = results.one()  # (3)!
        print("Hero 1:", hero_1)  # (4)!

        statement = select(Hero).where(Hero.name == "Captain North America")  # (5)!
        results = session.exec(statement)  # (6)!
        hero_2 = results.one()  # (7)!
        print("Hero 2:", hero_2)  # (8)!

        hero_1.age = 16  # (9)!
        hero_1.name = "Spider-Youngster"  # (10)!
        session.add(hero_1)  # (11)!

        hero_2.name = "Captain North America Except Canada"  # (12)!
        hero_2.age = 110  # (13)!
        session.add(hero_2)  # (14)!

        session.commit()  # (15)!
        session.refresh(hero_1)  # (16)!
        session.refresh(hero_2)  # (17)!

        print("Updated hero 1:", hero_1)  # (18)!
        print("Updated hero 2:", hero_2)  # (19)!
    # (20)!