def select_heroes():
    with Session(engine) as session:
        hero = session.get(Hero, 9001)
        print("Hero:", hero)