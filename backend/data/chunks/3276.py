@callback_router.get(
    "{$callback_url}/callback/", responses={400: {"model": CustomModel}}
)
def callback_route():
    pass  # pragma: no cover