def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        results = session.exec(statement)
        hero_1 = results.one()
        print("Hero 1:", hero_1)

        statement = select(Hero).where(Hero.name == "Rusty-Man")
        results = session.exec(statement)
        hero_2 = results.one()
        print("Hero 2:", hero_2)

        total_money = hero_1.money + hero_2.money
        print(f"Total money: {total_money}")