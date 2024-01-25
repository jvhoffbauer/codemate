@events_callback_router.get("{$callback_url}/events/{$request.body.title}")
def event_callback(event: Event):
    pass  # pragma: nocover