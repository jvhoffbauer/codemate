async def test_create_event(async_client: AsyncClient, event_counter, models):
    @event.listens_for(models.User, "before_insert")
    def receive_before_insert(mapper, connection, target):
        "listen for the 'before_insert' event"
        assert isinstance(target, models.User)
        event_counter.before += 1

    @event.listens_for(models.User, "after_insert")
    def receive_after_insert(mapper, connection, target):
        "listen for the 'after_insert' event"
        assert isinstance(target, models.User)
        event_counter.after += 1

    assert event_counter.before == 0
    assert event_counter.after == 0
    await test_route_create(async_client, models)
    assert event_counter.before > 0
    assert event_counter.after == event_counter.before