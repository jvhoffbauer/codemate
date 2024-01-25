    @event.listens_for(models.User, "after_insert")
    def receive_after_insert(mapper, connection, target):
        "listen for the 'after_insert' event"
        assert isinstance(target, models.User)
        event_counter.after += 1