    @app.post("/people/", response_model=PersonRead)
    def create_person(person: PersonCreate) -> Any:
        db_person = Person.model_validate(person)
        return db_person