async def test_update_event(
    async_client: AsyncClient, fake_users, event_counter, models
):
    @event.listens_for(models.User, "before_update")
    def receive_before_update(mapper, connection, target):
        "listen for the 'before_update' event"
        assert isinstance(target, models.User)
        event_counter.before += 1

    @event.listens_for(models.User, "after_update")
    def receive_after_update(mapper, connection, target):
        "listen for the 'after_update' event"
        assert isinstance(target, models.User)
        event_counter.after += 1

    @event.listens_for(models.User.username, "set")
    def receive_set(target, value, old, initiator):
        "listen for the 'set' event"
        assert isinstance(target, models.User)

    # update one
    assert event_counter.before == 0
    assert event_counter.after == 0
    await test_route_update(async_client, fake_users, models)
    assert event_counter.before > 0
    assert event_counter.after == event_counter.before