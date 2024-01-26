- Defines a function `create_hero` that takes in an argument of type `HeroCreate`.
- Uses SQLAlchemy's `Session` to interact with the database, and creates a new instance of the `Hero` model using its constructor (`Hero.model_validate`) with the input data from `hero`.
- Adds this newly created object to the session, commits the changes, and refreshes it to ensure all relationships are loaded properly before returning it.