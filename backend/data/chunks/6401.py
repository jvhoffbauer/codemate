async def test_delete_event(
    async_client: AsyncClient, fake_users, event_counter, models
):
    @event.listens_for(models.User, "before_delete")
    def receive_before_delete(mapper, connection, target):
        "listen for the 'before_delete' event"
        assert isinstance(target, models.User)
        event_counter.before += 1

    @event.listens_for(models.User, "after_delete")
    def receive_after_delete(mapper, connection, target):
        "listen for the 'after_delete' event"
        assert isinstance(target, models.User)
        event_counter.after += 1

    # delete one
    assert event_counter.before == 0
    assert event_counter.after == 0
    await test_route_delete(async_client, fake_users, models)
    assert event_counter.before > 0
    assert event_counter.after == event_counter.before