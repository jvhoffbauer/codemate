- Initializes connections during startup event using `@app.on_event("startup")`.
- Connects to Redis, initializes APScheduler scheduler, and connects to database (using SQLAlchemy).
- Closes the database connection during shutdown event using `@app.on_event("shutdown")`.