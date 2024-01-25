def test_dummy_webhook():
    # Just for coverage
    app.webhooks.routes[0].endpoint({})