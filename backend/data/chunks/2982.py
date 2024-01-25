async def get_database():
    temp_database = fake_database.copy()
    try:
        yield temp_database
        fake_database.update(temp_database)
    except HTTPException:
        state["except"] = True
    finally:
        state["finally"] = True