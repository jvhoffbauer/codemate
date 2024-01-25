def select_heroes():
    with Session(engine) as session:  # (7)!
        statement = select(Hero)  # (8)!
        results = session.exec(statement)  # (9)!
        for hero in results:  # (10)!
            print(hero)  # (11)!
    # (12)!