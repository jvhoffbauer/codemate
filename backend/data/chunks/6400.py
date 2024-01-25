    def receive_set(target, value, old, initiator):
        "listen for the 'set' event"
        assert isinstance(target, models.User)