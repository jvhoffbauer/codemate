def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson", money=1.1)
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", money=0.001)
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48, money=2.2)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()