    @event.listens_for(models.User, "after_delete")
    def receive_after_delete(mapper, connection, target):
        "listen for the 'after_delete' event"
        assert isinstance(target, models.User)
        event_counter.after += 1