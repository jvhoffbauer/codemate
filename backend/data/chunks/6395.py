    @event.listens_for(models.User, "before_update")
    def receive_before_update(mapper, connection, target):
        "listen for the 'before_update' event"
        assert isinstance(target, models.User)
        event_counter.before += 1