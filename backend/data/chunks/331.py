def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).join(Team).where(Team.name == "Preventers")
        results = session.exec(statement)
        for hero in results:
            print("Preventer Hero:", hero)