def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age > 32).offset(1).limit(2)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)