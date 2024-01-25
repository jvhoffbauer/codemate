    @app.post("/people/", response_model=PersonRead)
    def create_person(person: PersonCreate) -> Any:
        db_person = Person.from_orm(person)
        return db_person