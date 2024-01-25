@app.get("/pets/{pet_id}", response_model=PetOut)
async def read_pet(pet_id: int):
    user = UserDB(
        email="johndoe@example.com",
        hashed_password="secrethashed",
    )
    pet = PetDB(name="Nibbler", owner=user)
    return pet