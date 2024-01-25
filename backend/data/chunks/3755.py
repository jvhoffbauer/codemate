@app.webhooks.post("new-subscription")
def new_subscription(
    body: Subscription, token: Annotated[str, Security(bearer_scheme)]
):
    """
    When a new user subscribes to your service we'll send you a POST request with this
    data to the URL that you register for the event `new-subscription` in the dashboard.
    """