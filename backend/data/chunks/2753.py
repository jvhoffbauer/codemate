def test_required_noneable_body_embed_value():
    response = client.post("/body-embed", json={"b": "foo"})
    assert response.status_code == 200
    assert response.json() == "foo"