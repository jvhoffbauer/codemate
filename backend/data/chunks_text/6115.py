- Registers a listener function to be called after an `User` object is updated in SQLAlchemy's session.
- Verifies that the updated object is of type `models.User`.
- Incrementally increases a global counter named `event_counter.after` by one when this listener function is executed.