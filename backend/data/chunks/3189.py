    def create_person(person: PersonCreate) -> Any:
        db_person = Person.model_validate(person)
        return db_person