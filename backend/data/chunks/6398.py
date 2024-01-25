    def receive_after_update(mapper, connection, target):
        "listen for the 'after_update' event"
        assert isinstance(target, models.User)
        event_counter.after += 1