def test_required_nonable_body_embed_invalid():
    response = client.post("/body-embed", json={"invalid": "invalid"})
    assert response.status_code == 422