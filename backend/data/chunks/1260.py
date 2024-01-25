async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()