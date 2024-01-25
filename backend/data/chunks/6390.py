    @event.listens_for(models.User, "before_insert")
    def receive_before_insert(mapper, connection, target):
        "listen for the 'before_insert' event"
        assert isinstance(target, models.User)
        event_counter.before += 1