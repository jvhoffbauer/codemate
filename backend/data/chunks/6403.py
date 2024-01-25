    def receive_before_delete(mapper, connection, target):
        "listen for the 'before_delete' event"
        assert isinstance(target, models.User)
        event_counter.before += 1