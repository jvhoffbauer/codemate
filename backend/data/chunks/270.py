def select_heroes():
    with Session(engine) as session:
        hero = session.exec(select(Hero).where(Hero.name == "Deadpond")).one()
        print("Hero:", hero)