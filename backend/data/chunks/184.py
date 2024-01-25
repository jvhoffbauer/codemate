@app.on_event("startup")
def on_startup():
    create_db_and_tables()