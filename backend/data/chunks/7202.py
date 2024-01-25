def get_url() -> str:
    return "{scheme}://{user}:{password}@{host}/{db}".format(
        scheme="postgresql+asyncpg",
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        db=os.getenv("POSTGRES_DB"),
    )