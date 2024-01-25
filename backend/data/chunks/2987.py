@pytest.fixture(autouse=True)
def reset_state_and_db():
    global fake_database
    global state
    fake_database = initial_fake_database.copy()
    state = initial_state.copy()