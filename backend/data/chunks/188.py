@app.get("/heroes/", response_model=list[HeroRead])
def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes