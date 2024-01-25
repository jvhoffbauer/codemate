async def read_pets():
    user = UserDB(
        email="johndoe@example.com",
        hashed_password="secrethashed",
    )
    pet1 = PetDB(name="Nibbler", owner=user)
    pet2 = PetDB(name="Zoidberg", owner=user)
    return [pet1, pet2]