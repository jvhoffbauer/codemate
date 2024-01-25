    def inner(client):
        monkeypatch.setattr(
            client, "transport", _TestTransport(check_event, check_envelope)
        )