    @event.listens_for(models.User.username, "set")
    def receive_set(target, value, old, initiator):
        "listen for the 'set' event"
        assert isinstance(target, models.User)