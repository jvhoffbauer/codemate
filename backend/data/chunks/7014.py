def monkeypatch_test_transport(monkeypatch):
    def check_event(event):
        def check_string_keys(map):
            for key, value in map.items:
                assert isinstance(key, str)
                if isinstance(value, dict):
                    check_string_keys(value)

        with capture_internal_exceptions():
            check_string_keys(event)

    def check_envelope(envelope):
        with capture_internal_exceptions():
            # Assert error events are sent without envelope to server, for compat.
            # This does not apply if any item in the envelope is an attachment.
            if not any(x.type == "attachment" for x in envelope.items):
                assert not any(item.data_category == "error" for item in envelope.items)
                assert not any(item.get_event() is not None for item in envelope.items)

    def inner(client):
        monkeypatch.setattr(
            client, "transport", _TestTransport(check_event, check_envelope)
        )

    return inner