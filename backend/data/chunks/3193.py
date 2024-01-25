    def create_person(person: PersonCreate) -> Any:
        db_person = Person.from_orm(person)
        return db_person