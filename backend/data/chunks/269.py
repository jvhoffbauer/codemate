def select_heroes():
    with Session(engine) as session:
        hero = session.get(Hero, 1)
        print("Hero:", hero)