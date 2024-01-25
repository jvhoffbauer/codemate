def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).offset(6).limit(3)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)