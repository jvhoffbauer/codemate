def create_heroes():  # (1)!
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")  # (2)!
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:  # (3)!
        session.add(hero_1)  # (4)!
        session.add(hero_2)
        session.add(hero_3)

        session.commit()  # (5)!
    # (6)!